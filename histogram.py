fname = input("Enter file name: ")
try:
    fh=open(fname)
except:
    print('File mentioned does not exist')
    quit()
count=dict()
words=list()
for l in fh :
  line=l.rstrip()
  words=line.split()
  for word in words :
    count[word]=count.get(word,0)+1
maxwrd=None
maxval=None
for key,val in count.items():
    if maxval is None or val>maxval :
        maxval=val
        maxwrd=key
print('Maxword is',maxwrd)
print('Maxvalue is',maxval)
