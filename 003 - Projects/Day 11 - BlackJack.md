2025-12-07 15:38

Status: Complete

Tags: 


# Blackjack in Python

## Todo: Program Logic

## Code: Project Code

```
import random  
import sys  
from art import logo  
  
print(logo)  
  
while True:  
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()  
    if play_game != 'y':  
        print("Goodbye!")  
        break  
  
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
    user_hand = [random.choice(cards), random.choice(cards)]  
    computer_hand = [random.choice(cards), random.choice(cards)]  
  
    def calculate_score(hand):  
        score = sum(hand)  
        aces = hand.count(11)  
        while score > 21 and aces:  
            score -= 10  
            aces -= 1  
        return score  
  
    user_score = calculate_score(user_hand)  
    computer_score = calculate_score(computer_hand)  
  
    # Check for Blackjack  
    if computer_score == 21 and len(computer_hand) == 2:  
        print(f"Dealer's hand: {computer_hand}")  
        print("Dealer has Blackjack! You lose!")  
        continue  
    if user_score == 21 and len(user_hand) == 2:  
        print(f"Dealer's hand: {computer_hand}")  
        print("You have Blackjack! You win!")  
        continue  
  
    # Player's turn  
    while user_score < 21:  
        print(f"Your cards: {user_hand}, current score: {user_score}")  
        print(f"Dealer's first card: {computer_hand[0]}")  
        choice = input("Type 'y' to get another card, 'n' to pass: ").lower()  
        if choice == 'y':  
            user_hand.append(random.choice(cards))  
            user_score = calculate_score(user_hand)  
        else:  
            break  
  
    if user_score > 21:  
        print(f"Your final hand: {user_hand}, score: {user_score}")  
        print("You went over. You lose!")  
        continue  
  
    # Dealer's turn  
    print(f"Your final hand: {user_hand}, score: {user_score}")  
    while computer_score < 17:  
        computer_hand.append(random.choice(cards))  
        computer_score = calculate_score(computer_hand)  
  
    print(f"Dealer's final hand: {computer_hand}, score: {computer_score}")  
  
    # Determine winner  
    if computer_score > 21:  
        print("Dealer went over. You win!")  
    elif user_score > computer_score:  
        print("You win!")  
    elif user_score < computer_score:  
        print("You lose!")  
    else:  
        print("It's a draw!")

```

## References

