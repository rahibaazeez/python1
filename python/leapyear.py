year=int(input("Enter the year you want to display leapyear until which year  "))
for x in range(2024,year):
    if x%4==0 or x%400==0 and x%100!=0:    
        print("The leap years are ", x)
