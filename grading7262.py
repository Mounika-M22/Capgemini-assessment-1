# Student Grading System
# - Write a program to calculate and display student grades.
# - Input: Students name and marks for 5 subjects.
# - Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).
name=input("enter students name:\n")
a,b,c,d,e=map(int,input("enter students  marks of 5 subjects\n").split())
total=a+b+c+d+e
per=(total//5)
print(f'the students name is {name}\n')
print(f'students total marks are {total}\n')
print(f'students percentage is {per}%\n')
if per>90 and per<100:
    print(f'students grade is A')
elif per>80 and per<=89:
    print(f'the grade of student is B')
elif per>70 and per<79:
    print(f'the grade of student is C')
else:
    print("the student is fail")