from lxml import etree

text ='''<div> <ul> 
        <li class="item-1"><a>first item 你好</a></li> 
        <li class="item-1"><a href="link2.html">second item 你不好</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div>'''

#　将string 转换成element 节点对象
html = etree.HTML(text)
print(html)
print(etree.tostring(html).decode())

href_list = html.xpath("//li[@class='item-1']/a/@href")
text_list = html.xpath("//li[@class='item-1']/a/text()")
print(href_list)
print(text_list)
print('*'*10)
li = html.xpath("//li[@class='item-1']")
print(li)
print('*'*10)

# 合并 对应分组 把每个li的属性放入字典的方法
for li in html.xpath("//li[@class='item-1']"):
    temp = {}
    temp['href'] = html.xpath("//li[@class='item-1']/a/@href")[0] if li.xpath("./a/@href") else None
    temp['text'] = html.xpath("//li[@class='item-1']/a/text()")[0] if li.xpath("./a/text()") else None
    print(temp)