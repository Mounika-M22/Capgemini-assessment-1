# BMI Calculator
# - Develop a program to calculate BMI:
# - Input: Weight (kg) and height (m).
# - Output: BMI value and corresponding category (Underweight, Normal, Overweight,
# Obese).
weight,height=map(float,input("enter weight(kg) and height(m):\n").split())
bmi=(weight/height**2)
if bmi<18.5:
    print(f"you are underweight because of bmi {bmi}\n")
elif bmi>18.5 and bmi<24.9:
    print(f"you are normal because of bmi {bmi}\n")
elif bmi>=25 and bmi<29.9:
    print(f"you are overweight because of bmi {bmi}\n")
elif bmi>=30:
    print(f"you are obese because of bmi {bmi}\n")
else:
    pass