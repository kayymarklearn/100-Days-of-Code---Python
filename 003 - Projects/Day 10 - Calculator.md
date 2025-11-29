2025-11-29 22:02

Status: Incomplete

Tags: [[Day 10 - Functions with Outputs]]  [[Day 10 - Functions with outputs (code)]]


# Untitled

## Todo: Program Logic

## Code: Project Code

main.py
```
from art import logo  
  
def add(n1, n2):  
    return n1 + n2  
  
def subtract(n1, n2):  
    return n1 - n2  
  
def multiply(n1, n2):  
    return n1 * n2  
  
def divide(n1, n2):  
    return n1 / n2  
  
operations = {"+": add,  
              "-": subtract,  
              "*": multiply,  
              "/": divide,  
              }  
  
def calculator():  
    print(logo)  
    continue_using_result = True  
    first_number = float(input("Enter the first number: "))  
    while continue_using_result:  
        for key in operations:  
            print(key)  
        operator = input("Pick an operation: ")  
  
        second_number = float(input("Enter the second number: "))  
  
        result = operations[operator](first_number, second_number)  
  
        use_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()  
        if use_result == 'y' or use_result == 'yes':  
            first_number = result  
        else:  
            continue_using_result = False  
            print('\n' * 20)  
            calculator()  
  
calculator()
```


art.py
```
logo = r"""  
 _____________________|  _________________  |  
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |  
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |  
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |  
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |  
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |  
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |  
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |  
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |  
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |  
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' |_____________________|  
"""
```


## References

