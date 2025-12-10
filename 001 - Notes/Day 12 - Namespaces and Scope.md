2025-12-08 19:56

Status: Incomplete

Tags: [[Namespaces and Scope (code)]]


# Namespaces and Scope
## Scope
Local scope
> Variables (or functions) declared inside functions have local scope (also called function scope).
> They are only seen by other code within the same block of code.
> ```
> def my_function():
> 	my_local_var = 2
> # This will cause a NameError
> print(my_local_var)
> ```
 
Global Scope
> 
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.
```
my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
```

Global Variables
> You can force the code allow you to modify something with global if you use the global keyword before you use it.
>
>e.g. This will give you an error
>
a = 1
def my_function():
    a += 1
    print(a)
>
But this will work
>
a = 1
def my_function():
    global a
    a += 1
    print(a)


Global Constants
> You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to modify them.
>
 Naming Convention
>
Global constants are normally declared in ALL_CAPS with a underscore in between.
>
e.g.
>    
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

## References
