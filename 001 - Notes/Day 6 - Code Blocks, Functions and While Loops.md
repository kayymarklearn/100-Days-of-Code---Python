2025-11-22 20:54

Status: Incomplete

Tags: [[Day 6 - Code Blocks, Functions and While Loops (code)]]


## Functions
> A function in its simplest form is just a wrapper name for a block of code. You give it name and then when you call the function by that name, all the code within the function block will be executed. It can help us save time and reduce repeated code.

#### Defining a function
```
def <function name>():
    print("Hello")
    # Do something else
    # Do something else ...
```

#### Calling a function
> Calling a function just means triggering the function. We can call a function at any point in our code in Python.
`<function name>()`

##### Putting Everything together
```
#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function
```

> This code will result in the following sequence of output:
> Hello
   What is your name? #I type Angela
  Hello
  Angela  

## While Loops
> While something_is_true:
	Do something.
> The code only stops when something is no longer true.
> Use while loops when you don't care about where you are in a sequence.
> If the condition for the while loop is never met, it becomes an infinity loop (which means it runs till eternity or until it crashes.)



## References
[Karel the Robot](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json)
