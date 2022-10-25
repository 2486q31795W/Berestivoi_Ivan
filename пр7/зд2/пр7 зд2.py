arr = [0,1,2,3,4,5,6,7,8,9]
newarr =[]
for i in range(len(arr)):
    if(arr[i]%2!=0):
        newarr.append (arr[i])
i = len(newarr)-1
while i:
  print (newarr[i])
i-=1              