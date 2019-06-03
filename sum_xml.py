import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url=input('Enter location:')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_239120.xml'
print('Retrieving',url)
file=urllib.request.urlopen(url).read()
tree=ET.fromstring(file)
lst=tree.findall('.//count')
total=0
for num in lst:
    total=total+int(num.text)
print('sum:',total)
