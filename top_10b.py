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
lst=sorted([(v,k) for k,v in count.items()],reverse=True)
print(lst)
