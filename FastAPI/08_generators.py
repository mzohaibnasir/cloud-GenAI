"""
# Generators:
A generator is a special type of function that returns an iterator, which produces a sequence of values on demand. 
Instead of computing all values at once, a generator computes each value only when its next() method is called. 
This allows for efficient handling of large datasets, as only the current value is stored in memory.


# Lazy Execution:
Lazy execution is a technique where the evaluation of an expression is delayed until its value is actually needed. 
In Python, lazy execution is implemented using generators and iterators. When you create a generator or iterator, 
the code inside the generator or iterator is not executed until you start iterating over it. 
This allows for efficient handling of large datasets, as the code is only executed when needed.
    
"""


def mygenerator(n):
    for x in range(n):
        yield x**3  # will give next value everytime


values = mygenerator(100)  # returns iter
print(list(values))

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# for x in values:
#     print(x)
