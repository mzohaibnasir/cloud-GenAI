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


print_h1 = html_tag(tag="h1")  # first outer parameter
print_h1(msg="Hello")  # then inner parameter
print_h1(msg="Again")
