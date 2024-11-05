list1=[]
list2=[]
a=int(input("Enter number of elements in list : "))
for i in range(a):
     num=int(input("Enter the number"))
     list1.append(num)
for i in list1:
     if i>100:
         list2.append('over')
     else:
        list2.append(i)
print("List1 is " ,list1)
print(list2)
