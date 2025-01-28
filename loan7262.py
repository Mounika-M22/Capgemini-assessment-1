# Bank Loan Eligibility
# - Develop a program to check loan eligibility:
# - Input: Salary, age, and credit score.
# - Output: Loan approval or rejection with reasons.
salary,age,creditscore=map(int,input("enter salary , age , credit score respectively\n").split())
if age<21:
    print(f'the loan is rejected because you are {age} years old which is low\n')
elif creditscore<700:
    print(f'the loan is rejected because of low credit score {creditscore}\n')
elif salary<20000:
    print(f'loan is rejected because of low salary {salary}\n')
else:
    print(f"your loan is approved\n")