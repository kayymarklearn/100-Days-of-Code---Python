2026-01-01 11:41

Status: Incomplete

Tags: [[Day 20 - 21 - Class Inheritance & Slicing (code)]]
[[Day 20-21 - Snake Game]]



### **Class Inheritance**
> This is the process where a class takes properties (attributes) and functionality/methods from another class. Inheritance here is used in the general understanding of the work, like a child inheriting the eye or hair color of their parent.
> ```
> # say our Fish class inherits from an Animal class
> # the Fish class will be defined as
> class Fish(Animal):
> 	def __init__(self):
> 		super().__init__() # This initializes everything the super class (in this case Animal) can do in our Fish class.
> ```
> This allows us to take already created classes and extend their functionality without starting from scratch or rewriting code unnecessarily.


### **Slicing**
> This is a way of slicing (or taking part) of sequential data types (like strs, tuples or lists) in python
> ```
> keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
> keys[2:5] # takes only the members from 2nd index (inclusive) to 5th index (not inclusive)
> keys[2:]
> ```
## References
