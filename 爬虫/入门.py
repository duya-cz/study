from lxml import html

# 读取html文件
with open('resources\code.html', 'r', encoding='utf-8') as f:
    html_text = f.read()
    print(html_text) 

    # 解析文本，转换为一个文档对象
    document=html.fromstring(html_text) 

    # 解析表头，-xpath语法
    th_list=document.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # 获取表格内第一条数据
    td_list=document.xpath('//table/tbody/tr[1]/td/text()')
    print(td_list)

    # 获取表格内所有数据，每条元素每行显示
    tr_list=document.xpath('//table/tbody/tr')

    for tr in tr_list:
        tr_list_td=tr.xpath('./td/text()')
        print(tr_list_td)
        