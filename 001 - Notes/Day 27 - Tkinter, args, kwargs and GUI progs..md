2026-01-06 00:23

Status: Incomplete

Tags: [[Day 27 - Tkinter (GUI) and Advanced Args (code)]]


# **TKinter**
> its a python module primarily used for making GUI programs.
> TO USE:
> ```
> import tkinter
> window.title("My First GUI Program") # Change the tile of the program
>window.minsize(width=500, height=300) #Minimum size of the  window (default)
>window.mainloop() # Keep window on screen waiting for user interactions (always has to be at the every end of the program)
># Creating a label
>my_label = tkinter.Label(text="I am a label", font=(name, size, style))
>my_label.pack() # Places the label on the screen (automatically centered)
> ```

### Advance Python Arguments
### Arguments with default values
```
def my_func(a=1, b=2, c=3):
	#Do this with a
	#Then do this with b
	#then do this with c
	
	when the function is called without being given an argument, it uses the defaults specified.
```

#### Unlimited (positional) arguments
```
def add(*args): # args is the convention, but you can use whatever works for you.
	for n in args:
		print(n)

#Example 
def add(*numbers):
	return sum(numbers)

print(add(1, 2, 3, 4, 5 ,6, 7,8 ,9)) # Should print 45
```

#### Many (keyword) arguments {**Kwargs}
> Kwargs is a dictionary, that contains keyword parameters as keys and arguments as values
```
def calc(**kwargs):  
    print(kwargs)  
  
calc(add=3, mul=5) 
# This will print 
# {'add': 3, 'mul': 5}
```
> You can work with this as any dictionary. It allows you to select an argument to use when needed.
> ```
> class Car:  
    def __init__(self, **kwargs):  
        self.make = kwargs.get("make")  
        self.model = kwargs.get("model")  
  >	#get is used to get the value of a key from a dictionary, this method prevents error if the key does not exist.
car = Car(make="Nissan", model="GT-R")  
print(car.make)
> ```

#### Layout managers
> These are methods that allow us to determine the location of widgets on the scree.
> In, tkinter there's 3;
> pack, place and grid.
> - Pack: places all widgets on the screen right after each other in linear fashion
> - Place: uses (x, y) coordinates to determine where to place widgets relative to the size of the screen (it's very specific but impractical for projects with lots of widgets)
> - Grid: It imagines that the entire program is a grid that can be divided to an arbitrary number of rows and columns. You cannot use grid and pack in the same program.
> You can use, padx and pady in the component.config, to set padding for components.

## References
[Tkinter PyDocs](https://docs.python.org/3/library/tkinter.html)
[Tkinter Tutorial](https://www.pythonguis.com/tutorials/create-gui-tkinter/)


