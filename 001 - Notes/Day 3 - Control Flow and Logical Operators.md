2025-11-19 22:46

Status: Complete

Tags: [[Day 3 - Control Flow and Logical Operators (code)]] && [[Day 3 - Treasure Island]]


# **Control Flow & Logical Operators
#### Condition Check
> We can use Python to check a condition and tell the computer what to do in each case
> #Example 
> ```
> if <this condition is true>:
> 	<then execute this line of code.
> ```
> What if the Condition is false?
> 	The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.
> 	```
> 		if pigs can fly:
> 			<some code that will never execute>
> 		else:
> 			print("This is real life")
> 	```

#### Python Indentation
> Indentation is critical in python in order to make certain lines of code subsidiaries of other lines of code.
> #Example 
> ```
> if 5 > 2: # This is a parent line of code
> 	print("Yes") # This is a child line of code.
> ```
> Messing an indentation will lead to an #IndentationError which tells us that a line of code has not been properly indented.

#### Comparator Operators
> - > Greater than
> - < Less than
> - >= Greater than or equal to
> - <= Lesser than or equal to
> - == Equal to
> - != Not equal to
> #Note '=' is used for assignment and '==' is used to check equality.

#### Modulo Operator
> The modulo operator (%) gives the remainder of a division.
> 6 % 2 # will be 0
> 6 % 5 # will be 1
> 6 % 4 # will be 2

#### Nested If/Else Statement
> You can put if/else statements inside other if/else statements. This is known as nesting
> #Example 
> ```
> 
> If condition:
> 	  if another condition:
> 		  do this
> 	else:
> 		do this
> else:
> 	do this
> ```


#### if/elif/else
> This allows as to write many if statements to check different conditions that are unrelated to each other.
> ```
> input_number = int(input("Enter a whole number: "))  
 > 
mod_input_number = input_number % 2  
  >
if mod_input_number == 0:  
    print("even")  
else:  
    print("odd")
> ```

#### Logical Operators
> How to combine different conditions in the same line of code.
> There are three main logical operators
> - AND
> - OR
> - NOT
> ```
> 	A and B #Both conditions need to be true
	C or D #Only one condition needs to be true
	not E #The condition must be false
> ```


## References
