s=input("enter a string : ")
if s.endswith("ing"):
    a=s.replace("ing","ly")
else:
    a=s+"ing"
print(a)
