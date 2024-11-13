# 导入必要的库
import requests
from bs4 import BeautifulSoup
import os

# 输入要爬取的网页url
url = input("请输入要爬取的网页url: ")
protocol_and_domain = url[0:url.find("/",9)]

# 发送GET请求获取网页内容
response = requests.get(url)
response.encoding = 'utf-8'  # 指定编码格式为utf-8
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string

# 选择所有div标签，提取original-src属性值
img_urls = []
img_tags = soup.find_all('img')
for tag in img_tags:
    original_src = tag.get('original-src')
    if original_src:
        img_urls.append(protocol_and_domain + original_src)

# 指定保存图片的文件夹
folder_name = "C:\\Users\\31987\\Downloads\\" + title + "_downloaded_images"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# 依次下载图片并保存
for i, img_url in enumerate(img_urls):
    response = requests.get(img_url)
    with open(os.path.join(folder_name, f"{title}_image_{i:0>4}.jpg"), "wb") as f:
        f.write(response.content)
    print(f"第{i+1}张图片下载完成")

print("所有图片下载完成")