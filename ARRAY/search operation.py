def findele(arr,n,key)
for i in range(n):
  if(arr[i] ==key):
    return i;
return -1;
arr = [17,13,01,04,03]
key = 13
n = len(arr)
index=findele(arr, n, key)
if index != -1:
  print("Element Found at position: " + str(index + 1))
else:
  print("Element not found")
