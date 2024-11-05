x=[1,2,3,4,5,6,7,8,29]
print("The greatest number is  :",max(x))
c=max(x)
f='prime'
print("position ",(x.index(max(x))+1))
for i in range(2,c):
        if(c%i==0):
            f="Not Prime"
            break
print(f)
