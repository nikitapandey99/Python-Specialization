fname = input("Enter file name: ")
fh=open(fname)
count=0
for l in fh:
  line=l.rstrip()
  if line.startswith('From '):
    words=line.split()
    print(words[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")
