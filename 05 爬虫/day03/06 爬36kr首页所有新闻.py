import requests
import re
import json
url = 'http://36kr.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
}

response = requests.get(url=url,headers=headers)
html = response.content.decode()
json_str = re.findall(r"<script>var props=(.*?),locationnal=.*?</script>" ,html ,re.DOTALL)[0]

json_dict = json.loads(json_str)

news_list = json_dict['feedPostsLatest|post']

title_list = [i['title'] for i in news_list ]
print(title_list)