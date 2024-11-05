n=int(input("enter number"))
for i in range(1,n):
    print(i*"*")
for j in range(1,i):
    print(j*"*")
    i-=1
