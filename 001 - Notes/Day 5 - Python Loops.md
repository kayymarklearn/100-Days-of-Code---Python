2025-11-21 18:28

Status: Complete

Tags: [[Day 5 - Python Loops (Code)]]  [[Day 5 - Password Generator]]


# **For Loops
> Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.

### Syntax
```
for <variable name of each item> in <a List>:
    <do something>
    <do something else>
```

#### Indentation
> Indentation is very important in Python programming. Every time you see the : symbol used, you need to be careful about the indentation that comes afterwards.
#### Sum
> Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total).
#Example 
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
```

### For Loops with Range
> The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

##### Range Function
> range(1, 10), it can also take third parameter that defines the steps to jump.
> #Example range(1, 10, 2) # will print 1, 3, 5, 7, 9....
> This code doesn't do anything by itself. For example, if you tried printing, it would not  give any individual numbers. 
> But it can be used in conjunction with For Loops.
> #Example 
> ```
> for number in range(1, 10):
> 	print(number)
> 	# This will print the numbers 1 - 9. So the range can be expressed like this:
> 		'a <= range(a, b) < b'
> 		Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.
> ```

## References
