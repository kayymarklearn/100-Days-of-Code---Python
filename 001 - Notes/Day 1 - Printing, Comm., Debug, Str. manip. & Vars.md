2025-11-17 16:24

Status: Complete

Tags: [[Day 1 - Printing, Comment, Debug, Str. Manip & Vars (Code)]] && [[Day 1 - Band Name Generator]]


# **Printing, Commenting, Debugging, Str Manipulation & Variables**
#### syntax
## print() command.
>print() is a function used to output text inside the console.
	Use quotes or double quotes to tell the computer that the text is not code but rather normal strings.
	Strings as the name implies is a string of characters, the quotes or double quotes show the beginning and end of the text (string). Without the quotes the will be a #SyntaxError 



### String Manipulation
>End of Line character (end line): \n {Automatically moves to a new line and continues writing string there}
```
#Example: print("Hello World!\nHello World!")
```

Concatenation: Combine two or more different strings (make two or more strings one): +
```
#Example print("Hello" + "Angela"), #Remember that spaces are not automatically added.
```

#Note in python programming spaces are really really important. (Messing with them leads to #IndentationError .)

## Input command (function)
> input() is a function used to take user data., it takes a prompt for the user.
Data received by input() can be stored and used in the program. 
```
#Example input("What is your name?")
#Example 2; print("Hello" + input("What's your name?"))
```

## Comment
>Expressions that python will ignore
	Usually used to explain pieces of code or code logic
```
	print("hello")
	# This is a comment, the computer does not read this.
	# Use CTRL + / or Command + / to comment selected lines of code.
```

## #Variables
>Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. #Example inputs can be stored and used multiple times using variables.
As the name suggests, #Variables can be changed.
```
name = input("What is your name?")
print(name)
# We can use the variable name to refer to the data later on.
# It is similar to saving phoe numbers with names to make it easier to accessed.
name = "Mark"
print(name) # will print Mark.
name = "Jack"
print(name) # will now print Jack
```

## Naming Variables
>Rules to follow
	- Make sure the variable names are descriptive
	- Do not have spaces between words (use underscores)
	- Do not start with numbers (they can be used anywhere else in the name)
	- Do not use special words like print or input
	- Choose simple words that are less likely to become typos
	- Check the company style guidelines if you start to work at a company.
## References
[Python Documentation](https://docs.python.org/3/)
