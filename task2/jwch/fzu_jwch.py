import requests
import csv
import re
import time
import json
import os
from lxml import etree
from urllib.parse import urljoin


url='https://jwch.fzu.edu.cn'

with open('教务通知.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerow(['通知人','标题','日期','详情链接','附件名','附件下载次数','附件链接码'])

def parse_list_page(html,current_url):
    notices=[]

    pattern=r'<li>.*?(?:<span class="doclist_time">|<font[^>]*>)\s*(\d{4}-\d{2}-\d{2})\s*</(?:span|font)>.*?(【[^】]+】).*?<a\s+[^>]*?href="([^"]+)"[^>]*?(?:target="_blank")?[^>]*?title="([^"]+)"[^>]*>'
    matches=re.findall(pattern,html,re.DOTALL)

    for date,department,link,title in matches:
        full_link=urljoin(current_url, link.strip())
        title=re.sub(r'\s+', ' ', title.strip())
        notices.append({
            '通知人':department.strip(),
            '标题':title,
            '日期':date.strip(),
            '详情链接':full_link
        })
    return  notices


def attachment_download(file_id,owner_id,detail_url):
    if not file_id or not owner_id:
        return 0

    ajax_url="https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp"
    params={
        'wbnewsid':file_id,
        'owner':owner_id,
        'type':'wbnewsfile',
        'randomid':'nattach',
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        'Referer':detail_url,
        'X-Requested-With':'XMLHttpRequest',
    }
    res=requests.get(ajax_url,params=params,headers=headers,timeout=5)
    if res.status_code==200:
        data=res.json()
        return int(data.get('wbshowtimes',0))
    return 0


def get_attachment(detail_url,html):
    attachments=[]
    blocks = re.findall(r'<li[^>]*>(.*?)</li>', html, re.DOTALL)
    for block in blocks:
        name_=re.search(r'<a[^>]*>([\s\S]*?)</a>',block)
        href_ = re.search(r'href="(/system/_content/download.*?)"', block)
        if not name_ or not href_:
            continue
        name=name_.group(1).replace('附件【', '').replace('】已下载', '').strip()
        href=href_.group(1)

        owner_=re.search(r'owner=(\d+)', href)
        file_id_=re.search(r'wbfileid=(\d+)', href)
        if not owner_ or not file_id_:
            continue

        owner_id=owner_.group(1)
        file_id=file_id_.group(1)
        count=attachment_download(file_id, owner_id, detail_url)
        full_url=urljoin(detail_url, href)

        attachments.append({
            '附件名': name,
            '下载次数': count,
            '附件链接码': full_url,
        })
    return attachments


total=0
processed=0
max_pages=100
success=0
current_page=211

while total<500 and processed<max_pages:
    if processed==0:
        list_url=f'{url}/jxtz.htm'
    else:
        list_url=f'{url}/jxtz/{current_page}.htm'
        current_page-=1

    headers={'User-Agent':'Mozilla/5.0'}
    response=requests.get(list_url,headers=headers,timeout=15)
    response.encoding='utf_8'

    notices=parse_list_page(response.text,list_url)
    for notice in notices:
        if total>=500:
            break

        detail_headers = {'User-Agent': 'Mozilla/5.0', 'Referer': list_url}
        detail_response = requests.get(notice['详情链接'], headers=detail_headers, timeout=15)
        detail_response.encoding = 'utf-8'
        attachments = get_attachment(notice['详情链接'], detail_response.text)
        attachment_names = [att['附件名'] for att in attachments]
        attachment_counts = [str(att['下载次数']) for att in attachments]
        attachment_links=[att['附件链接码']for att in attachments]

        with open('教务通知.csv', 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                notice['通知人'], notice['标题'], notice['日期'], notice['详情链接'],
                '; '.join(attachment_names) if attachment_names else '无附件',
                '; '.join(attachment_counts) if attachment_counts else '0',
                '; '.join(attachment_links) if attachment_links else '无',
            ])

        total+=1
        success+=1
        time.sleep(0.5)

    processed += 1
    time.sleep(1)

print(f"成功爬取: {success} 条通知")