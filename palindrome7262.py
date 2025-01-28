s=input()
res=""
for i in s:
    res=i+res
if s==res:
    print("palindrome")
else:
    print("not palindrome")