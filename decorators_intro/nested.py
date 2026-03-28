#
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# def calc(calc_func, n1, n2):
#     return calc_func(n1, n2)
#
# print (calc(multiply, 2, 4)) # prints 8
# # print(calc(subtract, 5,1)) # prints 4


# Nested functions [They can be nested inside other functions]
def outer_function():
    print("I'm outer")
    
    def nested_function():
        print("I'm inner")
    # nested function will run when run inside the outer functions
    # nested_function()

    # Returning a nested function
    return nested_function

# outer_function()
# if we try to call the inner function outside the outside function, we get a out of scope error.
# nested_function()
#
# But.... functions can also be returned from other functions
inner_function = outer_function()
inner_function()
