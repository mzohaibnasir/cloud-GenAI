class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __add__(self, other):
        return Person(f"{self.name}+{other.name}", self.age + other.age)

    def __repr__(self) -> str:
        """
        Official Representation:

        Aims for an unambiguous representation that can be used to recreate the object.
        Useful for debugging, introspection, and serialization.
        The default behavior for the repr() function.
        """
        print("__repr__")
        return f"name: {self.name}, age: {self.age}"

    def __str__(self) -> str:
        """
        (String Representation):
        Focuses on a human-readable representation of the object.
        Ideal for printing objects directly or displaying them to the user.
        The default behavior for the str() function and print() statements.
        """
        print("__str__")
        return f"name: {self.name}, age: {self.age}"

    def __len__(self):
        # Length is calculated as the combined length of name and age (strings)
        print(f"name: {len(self.name)} , age: {len(str(self.age))}")

        return len(self.name) + len(str(self.age))

    def __call__(self):
        print(f"{self} ~ Object is called")


# ////////////

p: Person = Person(name="Mike", age=10)
q: Person = Person(name="Leonard", age=100)
z: Person = p + q
# print(p)
# print(q)
print(repr(p))
print(len(p))
p()
del p
