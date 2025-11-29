2025-11-28 22:58

Status: Incomplete

Tags: [[Day 10 - Functions with outputs (code)]] [[Day 10 - Calculator]]


# **Day 10 - Functions with Outputs**
> We've seen functions with only an execution body, functions with inputs that allow for variation in execution of the function body and now we'll see the final form of functions. Functions that can have outputs.
   We've seen functions with only an execution body, functions with inputs that allow for variation in execution of the function body and now we'll see the final form of functions. Functions that can have outputs.

### Storing Functions as a Variable Value

You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8

In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

### Docstrings
> A pythonic way to create documentation in functions or blocks of code.

```
"""
	This is how to use docstrings in python
	use triple quotes. 
	
	Can be used for comments (not recommeded).
	Can also be used for pre-formatted text. 
"""
```
## References
