import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
url=input('Enter: ')
html=urllib.request.urlopen(url).read()
file=BeautifulSoup(html,'html.parser')

tags=file('span')

total=0
for tag in tags:
    total=total+int(tag.contents[0])
print(total)
