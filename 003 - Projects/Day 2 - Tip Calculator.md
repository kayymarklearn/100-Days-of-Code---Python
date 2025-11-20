2025-11-18 19:45

Status: Complete

Tags: [[Day 2 - Data Types, Type (checking & converting), Math Ops & Number Manip.]]  && [[Day 2 - Data Types, Type (checking & converting), Math Ops & Number Manip. (Code)]]


# {Title}}

## Todo: Program Logic
	- Greet the user
	- Ask the user the total bill amount.
	- Ask the user the tip percentage.
	- Ask the user the number of people paying the bill
	- Calculate the tip amount using the percentage given.
	- Add the total bill to the tip amount and store the result
	- Divide the result by the number of people paying the bill.
	- Output how much each person should pay.
	- #Note Round to 2 decimal places to make usability easier for users.

## Code: Project Code
```
print("Welcome to the tip calculator!")  
bill = float(input("What was the total bill? $"))  
tip = int(input("What percentage tip would you like to give? 10 12 15 "))  
people = int(input("How many people to split the bill? "))  
  
  
tip_amount = bill * (tip / 100)  
total_bill = bill + tip_amount  
  
individual_payment = round(total_bill / people, 2)  
  
print(f"Each person should pay: {individual_payment}")
```


## References

