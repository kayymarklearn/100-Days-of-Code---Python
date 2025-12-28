2025-12-24 12:34

Status: Incomplete

Tags: [[Day 17 - OOP (Code)]]


# **How to create your own classes**
#### Class
> A class is a blue print for creating objects.
> Creating a function is similar to declaring a function. But we use PascalCase for classes not camelCase or snake_case.
> In python classes = PascalCase and any other thing = snake_case.
> Example;
> 	```
> 	class User:
> 		pass
> 		
>	user_1 = User()
> 	```
> In other to use attributes , we Use constructors (Initialize the object.)
> In python we use the '__init__(self)' method to initialize attributes
> Example;
> ```
> class Car:
> 	def __init__(self, name, age):
> 		Initialize attributes
> 		self.name =  name
> 		self.age = age
> car_1 = Car("Elantra", 10)
> ```
> #Note The __init__ function is called every time we create a new object.
>
> To Create methods (function in an object)
> ```
> > class Car:
> 	def __init__(self, name, age):
> 		Initialize attributes
> 		self.name =  name
> 		self.age = age
> 	def enter_race_mode(self):
> 		self.name = "John"
> car_1 = Car("Elantra", 10)
> car.enter_race_mode()
> ```
> Methods need to always have the self parameter


## References
