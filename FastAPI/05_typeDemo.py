# pip install mypy
# mypy app.py
def myfunction(parameter: int):
    print(parameter)


def returnString(parameter: int) -> str:
    return f"{parameter+12}"


# return list
def deos(param: list[int]):  # int is type
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


myfunction(1)  # will still act even if `parameter:int`
# print(returnString(11))
returnString(11)
print(deos([0, 0, 0]))
