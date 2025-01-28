def factorial(n):
    if n < 0:
        print("Error: Negative numbers not allowed.")
    res = 1
    for i in range(1, n + 1):
        res*= i
    return res

num = int(input("enter a number: "))
print(f"factorial: {factorial(num)}")