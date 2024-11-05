vowels='AEIOUaeiou'
L=[]
w=input("enter the word")
for i in w:
    if i in vowels:
        L.append(i)

print("The vowel letters are ", L)

