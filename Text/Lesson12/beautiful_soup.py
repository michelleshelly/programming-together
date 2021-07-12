import urllib.request as request
import urllib.parse as parse
import urllib.error as error

from bs4 import BeautifulSoup

url = 'http://dr-chuck.com/page1.htm'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#parser is a function that interpretes strings

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))