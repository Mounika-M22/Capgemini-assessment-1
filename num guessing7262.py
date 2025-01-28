# Number Guessing Game
# - Develop a program where the computer generates a random number between 1 and 100,
# and the user guesses the number.
# - Provide hints like Too High or Too Low.
# - Use a loop to allow multiple attempts.
import random
computer_num=random.randint(1,100)
while(True):
    user=int(input("enter a num for guess:\n"))
    if(computer_num-user>10):
        print(f'the guessed num {user} is too low')
    elif(computer_num-user<10 and computer_num-user>0):
        print(f'the num {user} is somewhat nearer')
    elif(computer_num-user<0):
        print(f'the guessed num {user} is too high')
    elif(computer_num-user==0):
        print(f'the guessed num {user} is correct')
        break

