# Find Second Largest Number
# - Write a program to find the second largest number in a list provided by the user.
# a=list(map(int,input("enter list:\n").split()))
# a.sort()
# print(f'the second largest is {a[(len(a)-2)]}')
#2 3 14 5 6
def secondlargest(arr):
    l1=arr[0]
    l2=arr[1]
    for i in range(len(arr)):
        if arr[i]>l1:
            l1=l2
            l2=arr[i]
        elif arr[i]>l2:
            l2=arr[i]
    print(l1)
arr=list(map(int,input("enter list elements: ").split()))
secondlargest(arr)