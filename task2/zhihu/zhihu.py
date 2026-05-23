import time
import csv
import re
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

driver_path = r"msedgedriver.exe"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 关闭“自动化提示”
options.add_experimental_option("useAutomationExtension", False)  # 禁用自动化扩展
options.add_argument("--disable-blink-features=AutomationControlled")  # 隐藏webdriver特征
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")

driver = webdriver.Edge(service=Service(driver_path), options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});    # 伪造插件列表
        Object.defineProperty(navigator, 'languages', {get: () => ['zh-CN', 'zh']});  # 伪造语言
    """
})

url = "https://www.zhihu.com/topic/19554298/top-answers"
driver.get(url)
input("登录成功后按 Enter 继续...")

question_urls = []
question_titles = []

links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/question/']")
for link in links:
    href = link.get_attribute("href")
    if href:
        m = re.search(r'(https://www\.zhihu\.com/question/\d+)', href)
        if m and m.group(1) not in question_urls:
            title_ = link.text.strip()
            if title_.startswith("问题"):
                continue
            question_urls.append(m.group(1))
            question_titles.append(title_)
    if len(question_urls) >= 20:
        break

results = []
for url, title in zip(question_urls[:20], question_titles[:20]):
    driver.get(url)
    time.sleep(3)
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    question_content = "无详细描述"
    for sel in ["div[class*='QuestionHeader-detail']", "div[class*='QuestionRichText']", "div.RichText"]:
        elems = driver.find_elements(By.CSS_SELECTOR, sel)
        for e in elems:
            txt = e.text.strip()
            if len(txt) > 10:
                question_content = txt[:500]
                break
        if question_content != "无详细描述":
            break

    answers = []
    items = driver.find_elements(By.CSS_SELECTOR, "div[class*='List-item']")
    for item in items:
        for sel in ["div[class*='RichContent-inner']", "div[class*='RichText']", "span.RichText"]:
            elems = item.find_elements(By.CSS_SELECTOR, sel)
            for e in elems:
                txt = re.sub(r'\s+', ' ', e.text.strip())
                if len(txt) > 30 and txt not in answers:
                    answers.append(txt[:1000])
                    break
            if len(answers) >= 10:
                break
        if len(answers) >= 10:
            break

    results.append({"title": title, "content": question_content, "answers": answers})
    time.sleep(3)

with open("zhihu_data.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["问题名", "问题具体内容", "回答信息"])
    for r in results:
        if r["answers"]:
            for a in r["answers"]:
                w.writerow([r["title"], r["content"], a])
        else:
            w.writerow([r["title"], r["content"], "无回答"])

print("爬取完成")