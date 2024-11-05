a=int(input("enter the number of names  "))
names=[]
for i in range(a):
 a=input("Enter the names")
 names.append(a)
print(names)
count1=0
for i in names:
    count=i.count('a')
    count1=count1+count
print("The letter 'a'appear count",count1)           
