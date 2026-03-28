# Python decorator functiony
import time
# def decorator_function(function):
#     def wrapper_function():
#         function()
#
#     return wrapper_function

# in order to add the delay to all functions, we can add the decorator
def delay_decorator(function):
    def sec_2_delay():
        time.sleep(2)
        # Do something before
        function()
        function() # you could even run it twice 😂
        print(function.__name__)
        # Do something after
    return sec_2_delay

# Now to apply decorator to all the function definitions we want to delay we can add the @decorator 

def say_hello():
    print("Hello 👋")

@delay_decorator
def say_bye():
    print("Bye 👋")

@delay_decorator
def say_greeting():
    print("How are your? 🫂")

say_hello()
say_bye()
say_greeting()

