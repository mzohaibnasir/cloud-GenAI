class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # def __del__(self):
    #     print("object is being destructed")

    def __add__(self, other):
        self.name = f"{self.name}+{other.name}"
        self.age = self.age + other.age
        return self.name, self.age


z = Person(name="x", age=1)
p = Person(name="Mike", age=10)
q = Person(name="Leonard", age=100)
print(p.name, p.age)
print(q.name, q.age)
z = p + q
print(z.name, z.age)
del p
