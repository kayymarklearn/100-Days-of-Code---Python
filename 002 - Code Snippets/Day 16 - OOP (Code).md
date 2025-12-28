2025-12-24 09:44

Status: Incomplete

Tags: [[Day 16 - OOP]]

# Code snippets and Examples

```
from turtle import Turtle, Screen

  
  

timmy = Turtle()

print(type(timmy))

  

my_screen = Screen()

timmy.color('burlywood4')

timmy.forward(100)

timmy.right(90)

timmy.forward(100)

timmy.right(90)

timmy.forward(100)

timmy.right(90)

timmy.forward(100)

print(my_screen.canvheight)

my_screen.exitonclick()
```

#### PrettyTable
```
  

from prettytable import PrettyTable

  

# Create an object from the PrettyTable class (Remember classes always use PascalCase)

table = PrettyTable()

  

# TODO 1 - Approach 1 [Using field_names and adding rows]

# table.field_names = ["Pokemon Name", "Type"]

# table.add_rows([['Pikachu', 'Electric'],['Squirtle', 'Water'], ['Charmander', 'Fire']])

  

# TODO 2 - Approach 2 [Adding each column]

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander']) # Use method

table.add_column('Type', ['Electric', 'Water', 'Fire']) # Use method

table.align = 'l' # Changing an attribute

print(table)
```