total=0
count=0
avg=0
while True:
  inp=input('Enter a number:')
  if inp == 'done':
    break
  try:
    n=int(inp)
  except:
    print('Invalid input')
    continue
  total=total+n
  count=count+1
avg=total/count
print(total,count,avg)
