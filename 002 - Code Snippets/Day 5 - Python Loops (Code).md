2025-11-21 18:29

Status: Incomplete

Tags: [[Day 5 - Python Loops]]  [[Day 5 - Password Generator]]

# Code snippets and Examples
#### For Loops #Example 
```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: 
# fruit here can be anything
# it is a variable that is assigned to the next element in each iteration of the loop.
	print(fruit)
# This will print out the elements of list in order
# Apple
# Peach
# Pear
	
```

#### Indentation
> This code will behave very differently

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

> from this code:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")
```

#### Sum function
```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
```

#### max function and min function (crude form)
> Returning the highest number from a list

```
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]  
# student_scores = [8, 65, 89, 86, 55, 91, 64, 89]  
highest_score = 0  
lowest_score = student_scores[0]  
  
# Determines the highest score  
for score in student_scores:  
    if score > highest_score:  
        highest_score = score  
  
# Determine the lowest score  
for score in student_scores:  
    if score < lowest_score:  
        lowest_score = score  
  
# Print out results  
print(f"The highest score is: {highest_score}")  
print(f"The lowest score is: {lowest_score}")

```

### FizzBuzz Game
> These are the rules of the FizzBuzz game:

  

> - Your program should print each number from 1 to 100 in turn and include number 100.      
   > 
>- But when the number is divisible by 3 then instead of printing the number it should print "Fizz".  
>
>- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`  
>
>- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
>
```
for number in range(1, 101):  
    if number % 3 == 0 and number % 5 == 0:  
        print("FizzBuzz")  
    elif number % 3 == 0:  
        print("Fizz")  
    elif number % 5 == 0:  
        print("Buzz")  
    else:  
        print(number)
```
