# OUC_IMG_Downloader

输入一个OUC文章网址，自动批量下载文章中的图片原图

## 1. 导入必要的库

```python
import requests
from bs4 import BeautifulSoup
import os
```

- requests: 用于发送HTTP请求，获取网页内容。

- BeautifulSoup: 一个用于解析HTML和XML文档的库，可以方便地提取网页中的数据。

- os: 用于与操作系统交互，特别是处理文件和目录相关的操作。

## 2. 输入要爬取的网页URL

```python
url = input("请输入要爬取的网页url: ")
protocol_and_domain = url[0:url.find("/",9)]
```

- input: 提示用户输入要爬取的网页地址。

- protocol_and_domain: 提取输入URL中的协议和域名部分，以便后续拼接出完整的图片链接。

## 3. 发送GET请求获取网页内容

```python
response = requests.get(url)
response.encoding = 'utf-8'  # 指定编码格式为utf-8
html_content = response.text
```

- requests.get(url): 发送一个GET请求到用户输入的URL，获取网页响应。

- response.encoding: 设置响应的编码为UTF-8，保证正确解析网页内容。

- html_content: 以文本形式获取网页的完整HTML内容。

## 4. 使用BeautifulSoup解析网页内容

```python
soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string
```

- BeautifulSoup(html_content, "html.parser"): 解析获取的HTML内容，并生成一个BeautifulSoup对象，以便后续提取数据。

- title: 获取网页的标题，后续下载的图片文件将使用该标题命名。

## 5. 选择所有img标签，提取original-src属性值

```python
img_urls = []
img_tags = soup.find_all('img')
for tag in img_tags:
    original_src = tag.get('original-src')
    if original_src:
        img_urls.append(protocol_and_domain + original_src)
```

- soup.find_all('img'): 查找所有<img>标签。

- 遍历所有图片标签，并获取其original-src属性，如果存在则将其拼接上协议和域名，存储在img_urls列表中。

## 6. 指定保存图片的文件夹

```python
folder_name = "C:\\Users\\31987\\Downloads\\" + title + "_downloaded_images"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
```

- folder_name: 根据网页标题生成保存图片的文件夹路径。

- os.path.exists(folder_name): 检查文件夹是否存在，如果不存在则创建该文件夹。

## 7. 依次下载图片并保存

```python
for i, img_url in enumerate(img_urls):
    response = requests.get(img_url)
    with open(os.path.join(folder_name, f"{title}_image_{i:0>4}.jpg"), "wb") as f:
        f.write(response.content)
    print(f"第{i+1}张图片下载完成")
```

- 遍历所有图片链接，发送GET请求并下载图片。

- 使用open函数创建并写入文件，每个图片文件名使用网页标题和序号命名 （``_image_{i:0>4}.jpg``，使序号属于四位数格式）。

- 下载完成后打印提示信息。

## 8. 结束提示
```python
print("所有图片下载完成")
```

- 当所有图片都下载完成后，输出提示信息告知用户。

- 通过这种方式，用户可以方便地从指定网页中下载所有图片，并自动保存到指定目录，这一过程大大简化了手动下载的步骤。
