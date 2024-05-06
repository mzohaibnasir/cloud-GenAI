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


def mydecorator(function):
    def wrapper():
        print("I am decorating your function")
        function()

    return wrapper


def hello_world():
    print("Hello World!")


mydecorator(hello_world)()


@mydecorator
def hello_world():
    print("Hello World!")


print("Using @")
hello_world()


print("##########################################")


def mydecoratorArgs(function):
    def wrapper(*args, **kwargs):
        print("I am decoratorArgs")
        function(*args, **kwargs)

    return wrapper


@mydecoratorArgs
def hello(person):
    print("Hello " + person)


hello("Ali")


#  to return wrapper


def mydecoratorArgsReturn(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
        print("Reachable?")  # this wont execute

    return wrapper


@mydecoratorArgsReturn
def hello(person):
    print("Hello " + person)


hello("XXX")


# so,

print("////////////////////////////////////")


def mydecoratorArgsReturnX(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("Reachable?")  # YES
        return return_value

    return wrapper


@mydecoratorArgsReturnX
def hellox(person):
    # print("Hello " + person)
    return f"Hello {person}"


print(hellox("XoX"))


print("\n\n\n\n LOGGGING:")


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open("logfile.txt", "a+") as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(1, 2))


# example 2

import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)  # we dont need function value
        after = time.time()
        f_name = function.__name__
        print(f"{f_name} took {after-before} seconds")
        return value

    return wrapper


@timed
def my(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


my(1000)
