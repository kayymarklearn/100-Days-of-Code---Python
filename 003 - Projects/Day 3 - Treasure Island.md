2025-11-20 00:47

Status: Complete

Tags:  [[Day 3 - Control Flow and Logical Operators]] && [[Day 3 - Control Flow and Logical Operators (code)]]


# Treasure Island


## Todo: Program Logic

![[Pasted image 20251120005038.png]]
## Code: Project Code
```
print(r'''  
*******************************************************************************  
          |                   |                  |                     | _________|________________.=""_;=.______________|_____________________|_______|                   |  ,-"_,=""     `"=.|                  |  
|___________________|__"=._o`"-._        `"=.______________|___________________  
          |                `"=._o`"=._      _`"=._                     | _________|_____________________:=._o "=._."_.-="'"=.__________________|_______|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |  
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________  
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              | _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |  
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________  
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____  
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____  
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_  
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____  
/______/______/______/______/______/______/______/______/______/______/_____ /  
*******************************************************************************  
''')  
print("Welcome to Treasure Island.")  
print("Your mission is to find the treasure.")  
direction = input('You\'re at a cross road. Where dd you want to go?\nType "left" or right"\n')  
  
if direction.lower() == "left":  
    lake = input('You\'ve come to the lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n')  
    if lake.lower() == "wait":  
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n')  
        if door.lower() == "red":  
            print("You were burned by a raging Inferno 🔥🔥. Game Over")  
        elif door.lower() == "blue":  
            print("You were eaten by hungry beasts 🦁🐯. Game Over.")  
        elif door.lower() == "yellow":  
            print("Hurray🥳🥳🙌. You're a champion.")  
        else:  
            print("Better luck next time. Game Over.")  
  
    else:  
        print("You were Attacked by an angry trout. Game Over.")  
else:  
    print("You fell into a hole. Game Over.")
```

## References

