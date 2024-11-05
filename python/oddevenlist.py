list1=[]
list2=[]
n=int(input("Enter the number of elements  "))
for i in range(n):
  num=int(input("Enter number  :"))
  if num%2==0:
      list1.append(num)
  else:
      list2.append(num)

print("Even number ",list1)
print("Odd numbers  ",list2)
