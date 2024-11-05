l=input("Enter a sentence ")
w=l.lower().split()
a={}
for i in l:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
for x,y in a.items():
print(x,y)
