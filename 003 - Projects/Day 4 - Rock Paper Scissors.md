2025-11-21 03:01

Status: Incomplete

Tags: [[Day 4 - Randomization and Python Lists]]  [[Day 4 - Randomization and Python Lists (code)]]  #IndexErrors 


# {Title}}

## Todo: Program Logic
- Ask the user to choose between; Rock, paper or scissors.
- Make a list of choices for the computer to choose from.
- randomly select one of the choices.
- Compare the user's selection to the random choice.
- write out the winner.

## Code: Project Code
```
	import random  
import sys  
  
rock = '''  
    _______---'   ____)  
      (_____)      (_____)      (____)---.__(___)  
'''  
  
paper = '''  
    _______---'   ____)____  
          ______)          _______)         _______)---.__________)  
'''  
  
scissors = '''  
    _______---'   ____)____  
          ______)       __________)      (____)---.__(___)  
'''  
  
computer_choice = random.choice(["Rock", "Paper", "Scissors"]).lower() # Randomly chooses a play for computer.  
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n") # Asks for user's play  
  
# Checking to make sure user input is legit  
if not user_choice.isdigit():  
    print("Unavailable choice. Game Over!")  
    sys.exit() # End the game immediately  
  
# make sure user input is a number  
user_choice = int(user_choice)  
  
# prints out the choice computer plays.  
def print_choice():  
    print(f'Computer chose:\n{globals()[computer_choice]}')  
  
# Outputs the hand both parties (user and computer) play.  
if user_choice == 0:  
    print(rock)  
    print_choice()  
elif user_choice == 1:  
    print(paper)  
    print_choice()  
elif user_choice == 2:  
    print(scissors)  
    print_choice()  
else:  
    print("Wrong choice. Game Over!")  
    sys.exit() # End the game immediately  
  
# Comparing the hands of each player and determining the winner.  
if (user_choice == 0 and computer_choice == "rock") or (user_choice == 1 and computer_choice == "paper") or (user_choice == 2 and computer_choice == "scissors"):  
    # All scenarios when the user wins  
    print("It's a draw!")  
elif (user_choice == 0 and computer_choice == "scissors") or (user_choice == 1 and computer_choice == "rock") or (user_choice == 2 and computer_choice == "paper"):  
    # All scenarios when there is a draw  
    print("You win!")  
else:  
    # All other scenarios (computer wins)  
    print("computer Wins!")
```



## References

