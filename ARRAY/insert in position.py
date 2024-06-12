def insertelement(arr,n,x,pos):
  for i in range(n-1,pos-1,-1):
    arr[i + 1] = arr[i]
  arr[pos] = x
arr = [17,13,28,1,4]
n = 4
print("before inserting:")
for i in range(0,n):
  print(arr[i],end=' ')
print("\n")
x = 3;
pos = 2;
insertelement(arr,n,x,pos)
n+=1
print("after inserting:")
for i in range(0,n):
  print(arr[i],end= ' ')
  
