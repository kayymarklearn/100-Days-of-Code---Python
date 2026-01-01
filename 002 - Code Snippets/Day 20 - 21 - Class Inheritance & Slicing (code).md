2026-01-01 11:51

Status: Incomplete

Tags: [[Day 20 - 21 - Class Inheritance & Slicing]]
[[Day 20-21 - Snake Game]]

# Code snippets and Examples

### Inheritance
```
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale.")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()  # prints out "Moving in water."
nemo.breathe()  # prints out "Inhale, Exhale."
print(nemo.num_eyes)  # prints out 2
```
> Methods can also be modified in the child class to have extra functionality.

```
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale.")
        
    
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
	    super.breathe() # This basically takes all functionality from the parent
	    print("Doing this underwater") # and extends or add more features to it.

    def swim(self):
        print("Moving in water.")
```