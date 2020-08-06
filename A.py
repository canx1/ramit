n=1
ct=0
print("Prime numbers between 0 to 100 are :")
while(n<=100):

  if n==2:
      print(n,end=" ")

  for i in range(2,n):
   if n%i==0:
     ct=0
     break
   else:
     ct=1

  if (ct>0):
     print(n,end=" ")
  n=n+1
