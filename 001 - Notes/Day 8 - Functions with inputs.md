2025-11-26 19:46

Status: Complete

Tags: [[Day 8 - Functions with inputs (Code)]] [[Day 8 - Caesar's Cipher]]

# **Functions that take input**
> Regular functions:
> ```
> def greet():  
    print("Hello customer.")  
    print("Welcome to our shop.")  
    print("Please choose what you wish to purchase.")  
    greet()
> ```

>Functions with inputs:
>By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.
>
That means we can modify how the function behaves each time by passing in different inputs.
>
># Creating the function
>def greet(input):
>	print(f"Hey! {input}")
># Using the function
>greet("Mark")
># Will output "Hey! Mark"

>Inputs are variables
>When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.
>
The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.
>
The value of the value of the input variable, e.g. Angela when you call the previous greet function: greet("Angela") is called the argument.
>
>Functions with multiple inputs:
>You can have multiple inputs in functions. All you need to do is separate them with a comma.
>```
>def greet_with(name, location):
>	print(f"Hello {name}, Welcome from {location}.")
>
>```

>Positional Arguments:
>By default, when you create a function in Python, it will keep the order of arguments in the function definition.
>Parameter 1 == Argument 1
>Parameter 2 == Argument 2
>```
># For example, with greet()
>	greet("Mark", "Accra") # name = "Mark", location = "Accra"
>	greet("Accra", "Mark") # name = "Accra", location = "Mark"
>```

> Keyword Arguments:
> You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.
> ```
> # For example, with greet()
> 	greet(location = "Accra", name = "Mark")
> ```
![[Pasted image 20251126200214.png]]


## References
[[Day 6 - Code Blocks, Functions and While Loops]]
[[Day 6 - Code Blocks, Functions and While Loops (code)]]