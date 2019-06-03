fname=input('Enter the file:')
try:
    fh=open(fname)
except:
    print('File mentioned is invalid')
    quit()
words=list()
count=dict()
for l in fh:
    line=l.rstrip()
    if line.startswith('From '):
        words=line.split()
        hour=words[5].split(':')
        count[hour[0]]=count.get(hour[0],0)+1
lst=list()
for k,v in count.items():
    lst.append((k,v))
srt=sorted(lst)
for k,v in srt:
    print(k,v)
