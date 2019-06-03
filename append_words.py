fname = input("Enter file name: ")

fh = open(fname)
lst = list()
for l in fh:
    line=l.rstrip()
    words=line.split()
    for wd in words:
        if wd in lst :
            continue
        lst.append(wd)
lst.sort()
print(lst)
