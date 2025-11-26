2025-11-26 19:47

Status: Incomplete

Tags: [[Day 8 - Functions with inputs]] [[Day 8 - Caesar's Cipher]]

# Code snippets and Examples

```
def greet(name, location):  
    print(f"Hello {name}.")  
    print(f"What is it like in {location}.")  
  
greet("Mark", "Akropong") # Positional Args  
  
greet(location = "Accra", name = "Johnson") # Keyword Args
```

#### Love interest calculator
```
name_of_person = input("What is your full name: ").lower()  
name_of_lover = input("What is the full name of your love interest: ").lower()  
  
def calculate_love_interest(name, lover):  
    true = 0  
    love = 0  
    for letter in "true":  
        for character in name:  
            if letter == character:  
                true += 1  
        for alphabet in lover:  
            if letter == alphabet:  
                true += 1  
    for letter in "love":  
        for character in lover:  
            if letter == character:  
                love += 1  
        for alphabet in name:  
            if letter == alphabet:  
                love += 1  
  
    print(true)  
    print(love)  
    print(f"Love Score = {true}{love}")  
  
calculate_love_interest(name_of_person, name_of_lover)
```