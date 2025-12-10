2025-12-10 22:10

Status: Complete

Tags:  [[Day 12 - Namespaces and Scope]]


# Number Guessing Game

## Todo: Program Logic
> Ask the user for the difficulty level  
Give them a number of chances based on difficulty level,  
Easy = 10 chances, Hard = 5 Chances  
Generate a random number  
for each chance allow the user to guess a new number  
compare the user's guess to the random number  
If they're the same, the user has won  
If user's guess is less, let them know  
If user's guess is more, let them know  
if user fails to guess the number after trying all the  
given number of chances, end the Game.

## Code: Project Code

art.py
```
logo = r"""  
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| """
```

main.py
```
import sys  
from art import logo  
import random  
  
print(f"{logo}")  
  
print(f"I'm thinking of a number between 1 and 100.")  
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()  
random_value = random.randint(1, 100)  
tries = 0  
if difficulty_level == 'easy':  
    tries = 10  
elif difficulty_level == 'hard':  
    tries = 5  
else:  
    print("Restart the game and choose a valid difficulty")  
    sys.exit(1)  
  
def guess(chances, random_number):  
    while chances > 0:  
        print(f"You have {chances} attempts remaining to guess the number.")  
        user_guess = int(input("Make a guess: "))  
        if user_guess == random_number:  
            print("You guessed the right number. You won!")  
            sys.exit(0)  
        elif user_guess > random_number:  
            chances -= 1  
            if chances == 0:  
                break  
            print(f"Too high.\nGuess again.")  
        elif user_guess < random_number:  
            chances -= 1  
            if chances == 0:  
                break  
            print(f"Too low.\nGuess again.")  
  
    if chances is 0:  
        print(f"You've run out of guesses. The right number is {random_number}. You lose!")  
  
guess(tries, random_value)

```


## References

