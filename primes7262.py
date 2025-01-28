# Prime Numbers in a Range
# - Write a program that takes two numbers as input and prints all the prime numbers in
# that range.
# - Use a function to check if a number is prime.

num1,num2=map(int,input("enter the 2 primes:\n ").split())
def checkprime(num1,num2):
    a=[]
    
    for i in range(num1+1,num2):
        if i<2:
            continue
        c=0 #reset c for every value while checking
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                c+=1
                break
        if c==0:
            a.append(i)
            
    print(f'the primes in range of {num1},{num2} are {a}')
checkprime(num1,num2)
