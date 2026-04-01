import requests
from lxml import html

# 定义网址
target_url="https://www.tiobe.com/tiobe-index/"

# 发送请求获取网页内容
response=requests.get(target_url)

# 输出数据到控制台
document=html.fromstring(response.text)

# 解析数据
th_list=document.xpath('//table[@id="top20"]/thead/tr/th/text()')
# 输出数据
print(th_list) 

# 解析表格数据
tr_list=document.xpath('//table[@id="top20"]/tbody/tr')
# 输出数据每条数据每列输出
for tr in tr_list:
    td_list=tr.xpath('./td/text()')
    print(td_list)
