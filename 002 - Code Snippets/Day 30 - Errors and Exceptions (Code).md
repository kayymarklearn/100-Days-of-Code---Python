2026-01-19 22:17

Status: Incomplete

Tags:  [[Day 30 - Errors, Exceptions and JSON Data]]

# Code snippets and Examples

> Catching Exceptions
```
#FileNotFound Error
try:
	file = open("a_file.txt")
except:
	file = open("a_file.txt", 'w')
	file.write("Something")
Using except here without specifying the error means that it will catch every type of error it encounters.
To be more specific specify the error you want to catch
except FileNotFoundError:
	do something
except KeyError as error_message:
	print(f"The key {error_message} does not exist")
```

> Raising Exceptions
> ```
> height = float(input("Height: "))
weight = int(input("Weight: "))
>
if height > 3:
    raise ValueError("Human Height should not be over 3 metres.")
>	# Raise an exception if condition is met.
bmi = weight / height ** 2
print(bmi)
> ```
