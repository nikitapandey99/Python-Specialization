fname=input('Enter a file:')
try:
    fh=open(fname)
except:
    print('File mentioned is invalid')
    quit()
words=list()
count=dict()
for line in fh:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
lst=list()
for k,v in count.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)
