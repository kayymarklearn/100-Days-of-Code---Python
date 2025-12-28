2025-12-24 15:11

Status: Incomplete

Tags: [[Day 18 - Graphics, Tuples and Models (Code)]]
[[Day 18 - Hirst spot color art]]

# **Turtle Graphics**
#### syntax
### Importing Modules
> ```
> import turtle
> tim = turtle.Turtle() # Basic import usage

> from turtle import Turtle
> tim = Turtle() # More convenient import statement.

> from turtle import * # Imports everything from the module
> tim = Turtle() # Not recommended practice
> ```

### How to alias modules (yes, give it an alias)
> Use the 'as' keyword
> import turtle as t
> tim = t.Turtle()

### Installing Modules
> Not all modules are packaged with the python standard library, therefore in other to use them, we need to install them

### Python Tuple
> Uses parenthesis (()), almost like a list but with round brackets
> Properties
> 1. Immutable (carved in stone): values cannot be changed.
> Trying to change its members will lead to a #TypeError 
> 2. It is essentially write once and read-only.
> ```
> my_tuple = (1, 2, 3, 4, 5)
>
print(my_tuple[0])

# my_tuple[0] = 10 # This will raise a TypeError because tuples are immutable
> ```
## References
[Python Sandbox](https://www.pythonsandbox.com/docs/turtle)
[TK color specification](https://www.tcl-lang.org/man/tcl8.4/TkCmd/colors.htm)
[Colors](http://cs111.wellesley.edu/reference/colors)
[Python package online -library](https://pypi.org/)
