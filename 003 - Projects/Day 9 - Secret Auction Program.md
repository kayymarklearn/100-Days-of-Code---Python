2025-11-27 21:58

Status: Complete

Tags:[[Day 9 - Dictionaries and Nesting]] [[Day 9 - Dictionaries and Nesting (Code)]]

# Secret Auction Program

## Todo: Program Logic
> 1. Ask the user for input  
> 2. Save data into dictionary {name: price}  
> 3. Whether if new bids need to be added  
> 4. ]Compare bids in dictionary

## Code: Project Code
#### main.py
```
import os
from art import logo  
  
  
print(logo)  
print("Welcome to the Blind Auction.")  
  
bidders = {}  
more_bidders = True  
  
while more_bidders:  
    user_name = input("what is your name: ")  
    user_bid = int(input("What is your bid: $"))  
  
    bidders[user_name] = user_bid  
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")  
  
    if new_bidder == 'no':  
        more_bidders = False  
  
    # print("\n" * 20)  
    os.system('clear')
  
  
high_score = max(bidders.values())  
  
for key in bidders:  
    if bidders[key]  == high_score:  
        print(f"The winner is {key} with a bid of ${high_score}")
```

#### art.py
```
logo = r'''  
                         ___________                         \         /                          )_______(                          |"""""""|_.-._,.---------.,_.-._                          |       | | |               | | ''-.                          |       |_| |_             _| |_..-'                          |_______| '-' `'---------'` '-'                          )"""""""(                         /_________\\                       .-------------.                      /_______________\\'''
```
## References

