n=int(input("Enter the numberof terms :"))
a=-1
b=1
for i in range(0,n):
 c=a+b
 print(c)
 a=b
 b=c
