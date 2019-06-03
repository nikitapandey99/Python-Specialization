import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input('Enter the url: ')
count=input('Enter count:')
count=int(count)

position=input('Enter position:')
pos=int(position)

while count>=1:
    print(url)
    url=urllib.request.urlopen(url).read()
    file=BeautifulSoup(url,'html.parser')

    tags=file('a')
    addr=tags[pos-1].get('href',None)
    count= count -1
    url =addr
print(url)
