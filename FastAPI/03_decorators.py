####################################################################################################
"""
Decorators add the fnction with additional functionality
decorator function is used to decorate other functions

It allow you to modify the behavior of functions without permanently altering their code. Here's a breakdown of how they work:

## Decorator Function:

1. A decorator is a function that takes another function as an argument and returns a modified version of that function.
2. This modified function typically has the same name and functionality as the original one, but with some additional behavior or modifications.

## Decorating a Function:

1. The @ symbol is used to apply a decorator to a function.
2. When you place a decorator @decorator_name above a function definition, Python treats it as if the function was wrapped by the decorator.
"""


# def mydecorator(function):
#     def wrapper():
#         print("I am decorating your function")
#         function()

#     return wrapper


# def hello_world():
#     print("Hello World!")


# print(mydecorator(hello_world)())
