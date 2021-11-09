n=int(input("number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev)
  print("the no. is a palendrome")
else:
  print("the no. is not apalendrome")