import requests

# 这是一个图片的url
url = 'http://yun.itheima.com/Upload/Images/20170614/594106ee6ace5.jpg'
response = requests.get(url)
# 获取的文本实际上是图片的二进制文本
img = response.content
# 将他拷贝到本地文件
with open( './a.jpg','wb' ) as f:
    f.write(img)
