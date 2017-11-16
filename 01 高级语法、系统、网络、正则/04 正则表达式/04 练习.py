#coding:utf8
import re

'''
需求：匹配出<html><h1>www.itcast.cn</h1></html>
'''
#res = re.search( "<(?P<t1>\w*)><(?P<t2>\w*)>.*</(?P=t2)></(P=t1)>","<html><h1>www.itcast.cn</h1></html>" )
res = re.search( "<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h1></html>" )
print(res.group())



'''
有一批网址：

http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
需要 正则后为：

http://www.interoem.com/
http://3995503.com/
http://lib.wzmc.edu.cn/
http://www.zy-ls.com/
http://www.fincm.com/
'''
res = re.search( r"http://[^/]+/","http://www.zy-ls.com/alfx.asp?newsid=377&id=6" )
print(res.group())


'''
有一句英文如下：
hello world ha ha
查找所有的单词
'''

resList =  re.findall("\w+","hello world ha ha")
print(resList)



'''
从下面的字符串中取出文本

<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
'''
html = "<div>     <p>岗位职责：</p><p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p><p><br></p><p>必备要求：</p><p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p><p>&nbsp;<br></p><p>技术要求：</p><p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p><p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p><p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p><p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p><p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p><p>&nbsp;<br></p><p>加分项：</p><p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p></div>"

res = re.sub(  "(</?\w*>)|(&.*;)","\n",html )
res = re.sub(  "\n\s*\n","\n",res )

print(res)