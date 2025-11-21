2025-11-21 00:54

Status: Complete

Tags: [[Day 4 - Randomization and Python Lists]] [[Day 4 - Rock Paper Scissors]]  #IndexErrors 

# Code snippets and Examples

#### Random Module
> To use: import random

```import random
random.randint (a, b)
# Generate a random number between a (inclusive) and b (inclusive)

random.random()
# takes no arguments
# Generate a random floating point number between 0 (inclusive) and 1 (!inclusive)
# To expand the scope, you can multiply the result by a whole number
#Example random.random()*10 will print between 0 and 10.

random.uniform(a, b)
# Works similarly to random.randint but also generates floating point numbers only.

random.choice([])
# Takes a sequence (lists, sets etc) and picks out a random one.
fruits = ["banana", "oranges", "papaya"]
print(random.choice(fruits)) # fetches an item at random.

random.shuffle([])
# randomly shuffles the members of a list 
li = ["Orange", "Guava", "Strawberry"]  
print(li)  
random.shuffle(li)  
print(li)
```

#### Lists
> Data structure
> Schema: List = [Item1, Item2, Item3]

```
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Indices
states_of_america[0] # Returns first state (Delaware).

#NegativeIndices
states_of_america[-1] #prints Hawaii, which is the last item
states_of_america[-2] #prints Alaska, which is second to last

#Modifying Items
states_of_america[1] = "Pencilvania" # alter an item just like a variable.

#Adding Items
states_of_america.append("New Item") # This function 'append()' adds a new item to the end of the list.

```
> Nested Lists
> ```
> fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
> ```
