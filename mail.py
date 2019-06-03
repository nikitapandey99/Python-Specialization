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
        count[words[1]]=count.get(words[1],0)+1
maxp=None
maxn=None
for per,no in count.items():
    if maxn is None or no>maxn:
        maxn=no
        maxp=per
print(maxp,maxn)
