# Odd and Even Separator
# - Write a program that takes a list of numbers as input and separates them into odd and
# even lists.
a=list(map(int,input("enter list of numbers:\n").split()))
odd=[]
even=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(f"the even numbers are {even}\nthe odd numbers are {odd}")