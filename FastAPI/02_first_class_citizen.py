"""First class functions
A language is said to have first class functions if it treats its functions as first class citizen. 
First-class citizen in a programming language is an entity which supports all the operations generally available to other entities(can be trateated like objects & variable). 
These operations typically include being passed as an argument, returned from a function and assigned to a variable.
"""

"""
ASSIGN FUNCTION TO VARIABLE
"""

# Assigned to a variable


def square(x):
    return x * x


f = square(5)
print(f"square: {square}")
print(f"f: {f}")


x = square
# print(x(11))
print(f"x(11): {x(11)}")


print(f"eval: {eval('x(25)')}")


"""
# HIGHER ORDER FUNCTION
function that accepts other functions as arguments and returns functions as a result
"""


l = [1, 2, 3]

x = lambda x: x * 2

print(list(map(x, l)))


"""RETURN A FUNCTION"""

"""
A closure in Python is a function that has access to its own scope and the scope of the functions in which it was defined.
This means that a closure can use variables from its own scope and from the scopes of the functions that created it, 
even when the closure is called outside of those functions.
Nested functions are able to access variables of the enclosing scope. """


def outer(msg):
    oh = 10

    def inner(i):
        print(f"msg: {msg} | oh: {oh}| i:{i}")

    return inner


log_hi = outer(msg="Hoye")
log_hi(i=99)


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Hello")
print_h1("Again")
