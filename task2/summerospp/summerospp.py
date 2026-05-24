import os
import json
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


url="https://summer-ospp.ac.cn"
driver=webdriver.Edge()
wait=WebDriverWait(driver, 10)


def parse_detail_page(detail_url):
    main = driver.current_window_handle
    driver.execute_script(f"window.open('{detail_url}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    info = {
        "brief": "",
        "output": ""
    }

    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "body")))
    time.sleep(1)

    try:
        brief_el = driver.find_element(By.XPATH, "//*[contains(text(), '项目简述')]/following-sibling::div")
        info["brief"] = brief_el.text.strip()
    except:
        info["brief"] = ""
    try:
        output_el = driver.find_element(By.XPATH, "//*[contains(text(), '项目产出要求')]/following-sibling::div")
        info["output"] = output_el.text.strip()
    except:
        info["output"] = ""

    driver.close()
    driver.switch_to.window(main)

    return info


projects=[]
list_url = f"{url}/org/projectlist?year=2025&pageNum=1"
driver.get(list_url)
time.sleep(2)
current_page = 1

while True:
    print(f"\n正在处理第{current_page}页")
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".ant-table-tbody tr")))
    rows = driver.find_elements(By.CSS_SELECTOR, ".ant-table-tbody tr")
    if not rows:
        break

    page_items = []
    for row in rows:
        try:
            tds = row.find_elements(By.TAG_NAME, "td")
            id = tds[0].text.strip()
            name = tds[1].text.strip()
            difficulty = tds[3].text.strip()
            tags = tds[4].text.strip()
            if id and name:
                page_items.append({
                    "id": id,
                    "name": name,
                    "difficulty": difficulty,
                    "tags": tags
                })
        except Exception as e:
            continue

    for item in page_items:
        detail_url = f"{url}/org/prodetail/{item['id']}?lang=zh&list=pro"
        detail_info = parse_detail_page(detail_url)
        data = {
            "id": item['id'],
            "name": item['name'],
            "difficulty": item['difficulty'],
            "tags": item['tags'],
            "brief": detail_info["brief"],
            "output": detail_info["output"]
        }
        projects.append(data)

    try:
        next = driver.find_element(By.CSS_SELECTOR, ".ant-pagination-next:not(.ant-pagination-disabled)")
        driver.execute_script("arguments[0].click();", next)
        current_page += 1
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".ant-table-tbody tr")))
        time.sleep(1)
    except Exception:
        print("到达最后一页")
        break

if projects:
    with open("projects_2025.json", "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)
    print(f"\n成功抓取 {len(projects)} 个项目")

driver.quit()