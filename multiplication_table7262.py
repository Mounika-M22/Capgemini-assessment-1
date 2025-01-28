# Multiplication Table Generator
# - Create a program to generate a multiplication table for any number provided by the user.
# - Allow the user to specify the range of the table.
table=int(input("enter number for multiplication table:\n"))
range1=int(input("enter range for table:\n"))
for i in range (1,range1+1):
    print(f'{table} x {i} = {table*i}')

