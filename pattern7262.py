n=int(input("enter n for number of rows:\n"))
for i in range(1,n+1):
    print(f'{'*'*i}')
print("the reverse pattern is:\n")
for i in range(n,0,-1):
    print(f'{'*'*i}')
