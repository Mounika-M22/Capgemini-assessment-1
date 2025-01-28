# Leap Year Checker
# - Write a program to check if a given year is a leap year.
# - Allow the user to check multiple years.
a=list(map(int,input("enter years to check for leap or not:\n").split()))
for i in range(len(a)):
    if a[i]%4==0 and a[i]%100!=0:
        print(f'the year {a[i]} is leap year\n')
    elif a[i]%400==0 and a[i]%100==0:
        print(f'the year {a[i]} is leap year\n')
    
    else:
        print(f'the year {a[i]} is not a leap year\n')