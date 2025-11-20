2025-11-18 19:40

Status: Complete

Tags: [[Day 2 - Data Types, Type (checking & converting), Math Ops & Number Manip. (Code)]]  && [[Day 2 - Tip Calculator]]


# **Data Types, Type Error (checking and conversion), Mathematical Operations, Number Manipulation**
### Data Types
> Data types in Python are a way to classify data items. They represent the kind of value, which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.
![[Python-Data-Types.webp]]
#Code #Example:
```
x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
```

#Strings
> Characters in quotes even if they are numbers.
	#Example 123 are not strings but "123" is a string.
	#TypeError 
```
"Hello"[0] #This is called subscripting or Indexing, we always start from zero for first character in the string.

#Example print("Hello"[1]) # This will print 'e'.

#Note [-1], Always prints out the last character.
#Example print("Hello"[-1]) #Will print out 'o'. We can keep counting backwards in this manner. 
```

#Integer = Whole Numbers
> Numeric Characters without quotes. #Example 123, 450, 244.
	Large #Integer 
		We can replace comas in long numbers with underscores for easier visualization. 
```
x = 123 #Integer 
#large Integer
print(123_456_235_234) # python will print 123456235234
```


#Float = Floating Point Number
> Basically decimal Numbers ('Floating' because the decimal point can be anywhere in the number)
```
x = 3141.59 #Float 
```

#Boolean = True/False, 1/0 ...
> Always written with the first letters being Capital letters. They very useful for logic statements and comparison.
```
True #Bool
False #Bool
```

### Type Error, Type Checking and Type Conversion
#[
>These errors occur when using wrong data types.
>#Example lean(12345) Gives this error  because len() expects strings not integers.

#Type 
> Is a function that tells the data type of a given object or data.
> ```
> print(type("Hello")) # outputs '<class 'str'>'.
> ```
> #TypeChecking is using the #type function to tell the type of a piece of data or object.

#TypeConversion || #TypeCasting
> This is converting or changing the datatype of a data object to another type.
> For instance from string to integer.
> ```
> print("123" + 123) #will give a #TypeError error because they're diff datatypes.
> Fix: print(int(123) + 123) #will print 246. They both integers now
> ```
> Not all data can be converted, for instance converting the string 'abc' to integer will give an error call #ValueError.
> - Use int() to convert to integers
> - Use str() to convert to strings.
> - Use float() to convert to floats
> - Use bool() to convert to Boolean.


### Mathematical Operators
> Python allows the use of all these math operations using  `+, -, *, /, // and **`
> Python uses the order of priority PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction) when doing evaluating mathematical expressions. When there is an expression to be evaluated, the left most takes precedence for Mul/Div and Add/Sub.

#### Syntax
```
print(12 + 12) #Addition
print(7 - 3)   #Subtraction
print(3 * 2)   #Multiplication
print(6 / 3)   #Division #Python implicitly #Typecastes divisions to floats.
print(6 // 3)  # This division operator prevents implicit #TypeCasting. Using this will affect the accuracy of results because decimals will be removed.

print(2 ** 4)    #Exponent; 2*2*2*2

# PEMDAS #Example 
print(3 * 3 + 3 / 3 - 3) #will print out 7
#Note PEMDASLR [Left to Right]; Expressionsin brackets are run first
print(3 * (3 + 3) / 3 - 3) #will now print 3 because it evaluates the brackets first.

```


### Number Manipulation and F strings
> Flooring a Number
> 	We can floor a number or remove all decimal places using the int() function which converts floating point numbers into a whole number.
> 			`int (3.7384) becomes 3`
> 			
> Rounding a Number
> 	However if you want to round a decimal number to the nearest whole number using the tradition math way, where anything over .5 rounds up and anything below runs down. Then you can use the round() function.
> 			`round(3.845) becomes 4`
> 			`round(3.234) becomes 3`
> 		round() takes 2 parameters, first one is the number to round and the second tells how many decimal places to round to.
> 		
> Assignment Operator
> 	Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
> 	+= ,-=,  *= /= 
> 	#Code 
> 	```
> 		score = 0
> 		score += 3
> 		print(score) # 3
> 		score -= 1
> 		print(score) # 2
> 	```
> f-strings
> 	In Python, we can use f-strings to insert a variable or an expression into a string.
> 	```
> 		age = 12
> 		print(f"I am {age} years old") # Will ouput I am 12 years old.
> 	```
> 


## References
[Data Types](https://www.geeksforgeeks.org/python/python-data-types/)
[Python Documentation](https://docs.python.org/3/)
[Floating Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html)
