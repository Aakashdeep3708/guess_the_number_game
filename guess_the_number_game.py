import random

random_number=random.randint(1,100)

print("Welcome to the Number Guessing Game")
print("Think of a number between 1 and 100\n")
level=input("Choose a difficulty. Type 'easy' or 'hard':")

def easy():  
    not_correct=True
    attempt=10
    while not_correct:
        if attempt!=0:
            guess=int(input("Make a guess:"))
            if guess==random_number:
                print("You guess the right number")
                not_correct=False
            elif guess>random_number:
                print("You guessed too high")
                attempt-=1
                print(f"remaining attempts {attempt}")
            else:
                print("You guessed too low")
                attempt-=1
                print(f"remaining attempts {attempt}")
        else:
            not_correct=False
            print("You loose the game")
            print(f"The correct number is {random_number}")
            
def hard():  
    not_correct=True
    attempt=5
    while not_correct:
        if attempt!=0:
            guess=int(input("Make a guess:"))
            if guess==random_number:
                print("You guess the right number")
                not_correct=False
            elif guess>random_number:
                print("You guessed too high")
                attempt-=1
                print(f"remaining attempts {attempt}")
            else:
                print("You guessed too low")
                attempt-=1
                print(f"remaining attempts {attempt}")
        else:
            not_correct=False
            print("You loose the game") 
            print(f"The correct number is {random_number}")   
    
    
if level=="easy":
    print("You have 10 attempts to guess the number")
    easy()
    
elif level=="hard":
    print("You have 5 attempts to guess the number")
    hard()