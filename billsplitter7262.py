# Bill Splitter
# - Create a program to split a bill among a group of people:
# - Input: Total bill amount, number of people, and any tip percentage.
# - Output: Amount each person has to pay.
bill,people,tippercent=map(int,input("enter total bill , no of people , tip percent respectively\n").split())
total_bill=bill+(bill*(tippercent/100))
print(f'each person has to pay {total_bill/people} amount')
