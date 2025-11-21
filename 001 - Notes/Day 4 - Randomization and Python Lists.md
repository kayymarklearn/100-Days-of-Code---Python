2025-11-21 00:49

Status: Complete

Tags: [[Day 4 - Randomization and Python Lists (code)]]  [[Day 4 - Rock Paper Scissors]]  #IndexErrors 

# Randomization and Lists in Python

#### Random Module
> In other to generate random numbers in python we use the random module which technically generates pseudo-random numbers.
> ```
> import random # We first have to import it to use functions under it.
> # Use random.randint(a, b) a: start number, b: end number (basically a range).
> random.randint(1, 10) # will give random numbers between 1 and 10 (including 10).
>
> # Random floating point numbers
> random.random() # does not take any input at all
> random.random() # prints floating point numbers between 0 (inclusive) and 1 (!inclusive)
>
>random.uniform(a, b) # return a random floating point number between a (inclusive) and b (inclusive).
>random.shuffle(list) #shuffle the members of a list
>usage:
>	li = ["Apple", "Orange", "Pawpaw"]
>	random.shuffle(li)
> 
> ```

##### What is a module?
> A module is a small piece of code with that deals with specific functionality, that can be put together to get a final program.
>
>To create a module:
>- Create a .py file (the file name is the name of the module Eg. my_module.py)
>- Write you code in the file
>- Use the import command to import the file in other files (Eg. import my_module)
>- You can use functions from your module buy using
>```import my_module
>print(my_module.favnumber_gen())
>```


#### Python Lists
> Lists are Data Structures in python; which simply means its a way of storing data.
> - It's used to store grouped pieces of data; #Example storing all the names of learners in a class.
> - It stores data in order. This order is very important.
> - They can store data of different types.
> - Lists are indexed like strings 
> - The individual items can be modified
> - New items can be added.
> - Items can be removed.
> ```
> #Example 
> fruits = [item1, item2]
> fruits = ["banana", "oranges", "cherries"]
> ```
>
>Lists Within a List (Nested Lists)
>fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
>


## References

Randomization
[Random function documentation](https://docs.python.org/3/library/random.html)
[Random Vs Pseudo-random Number generators](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
[Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)


Python Lists
[Lists documentation](https://docs.python.org/3/tutorial/datastructures.html)
#IndexErrors 
