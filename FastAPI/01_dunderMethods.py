class Person:
    def __init__(self, name: str = None, age: int = None):
        self._name = name
        self.age = age

    def __del__(self):
        print("Obj is being distructed")


p = Person(name="Mike", age=10)
print(p._name, p.age)
del p
