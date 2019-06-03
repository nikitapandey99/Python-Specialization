import re
fname=input('Enter the file:')
if len(fname) < 1 : fname = "regex_sum_282730.txt"
fh=open(fname)
lst=list()
total=0
for line in fh:
    x=re.findall('[0-9]+',line)
    for z in x:
        total=total+int(z)
print(total)
