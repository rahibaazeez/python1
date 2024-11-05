names=[]
list2=[]
for i in range(5):
   name=input("Enter name :")
   names.append(name)
for name in names[:]:
 if name[0]=="A" or name[0]=="a":
     list2.append(name)
     names.remove(name)
print("Name starting with A is  :",list2)
       break
print("Names after removing",names)
    
    
