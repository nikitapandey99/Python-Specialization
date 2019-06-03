import urllib.request, urllib.parse, urllib.error
import json

url=input('Enter location: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_239121.json'
file=urllib.request.urlopen(url).read()
print('Retrieving:',url)

print('Retrieved',len(file),'characters')

js=json.loads(file)
lst=js["comments"]
total=0
for item in lst:
    total=total+int(item["count"])

print('Count:',len(lst))

print("Sum:",total)
