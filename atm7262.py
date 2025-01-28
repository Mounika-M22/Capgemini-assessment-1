# ATM Simulation
# - Create a program to simulate an ATM where users can:
# - Check balance
# - Deposit money
# - Withdraw money
# - Exit
# - Use functions for each operation and implement proper input validation (e.g., insufficient
# balance for withdrawal).

money=int(input("enter the money in the bank::"))

while(True):
    option=int(input("enter the operation you want to perform::\n1.deposit \n2.withdraw\n3.check balance\n4.exit\n"))
    match option:
        case 1:
            dep=int(input("enter the amount to be deposited::"))
            def deposit(a):
                print(f'the deposited money is {dep}')
                return dep
            x=deposit(dep)
            money=money+x
            
            exit
        case 2:
            draw=(int(input("enter the money to be taken::")))
            def withdraw(b):
                print(f'the money withdrawn is {draw}')
                return draw
            y=withdraw(draw)
            money=money-y
            
            exit
        case 3:
            def check():
                balance=money
                print(f'the balance is : {balance}')
            check()
            exit
        case 4:
            print("exiting")
            break

    
            
        







