2025-11-21 19:35

Status: Complete

Tags: [[Day 5 - Python Loops]]  [[Day 5 - Python Loops (Code)]]

# Password Generator

## Todo: Program Logic
* Greet the user.
* Ask how many letters to use in password
* Ask how many symbols to use in the password
* Ask how many numbers to use in the password
* Select random letters from the list of English alphabets
* Select random numbers and symbols from the list of numbers and symbols
* #Easy concatenate all to form a strong password
* #Difficult randomly concatenate all to form strong password
* Output the password for the user.

## Code: Project Code
```
import random  
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  
  
print("Welcome to the PyPassword Generator!")  
nr_letters = int(input("How many letters would you like in your password?\n"))  
nr_symbols = int(input(f"How many symbols would you like?\n"))  
nr_numbers = int(input(f"How many numbers would you like?\n"))  
  
# Declare variables to store random characters  
chosen_letters = ''  
chosen_symbols = ''  
chosen_numbers = ''  
hard_password = ''  
  
# Choose random letters  
for i in range(0, nr_letters):  
    chosen_letters += random.choice(letters)  
  
# Choose random symbols  
for i in range(0, nr_symbols):  
    chosen_symbols += random.choice(symbols)  
# Choose random digits  
for i in range(0, nr_numbers):  
    chosen_numbers += random.choice(numbers)  
  
# Easy version  
easy_password = f'{chosen_letters}{chosen_symbols}{chosen_numbers}'  
print(f"Your new, easy password is: {easy_password} ")  
  
# Difficult version  
for character in easy_password:  
    hard_password += random.choice(easy_password)  
  
print(f"Your new, hard password is: {hard_password}")
```


## References

