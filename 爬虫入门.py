import requests
from bs4 import BeautifulSoup


# baidu=requests.get('http://www.baidu.com').content
# soup=BeautifulSoup(baidu,'html.parser')
# links=soup.find_all('a')
# for link in links:
#     print(link.string)

data=requests.get('https://www.zhihu.com/explore').content
soup=BeautifulSoup(data,'html.parser')
print(soup.body.div.attrs)
