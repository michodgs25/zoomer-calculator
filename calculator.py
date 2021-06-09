def calculator(a, b):
    print(f"CALCULATING {a}, {b}")
    return a, b


# create add function, return additional sum
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


# create subtract function, return subtracted sum
def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b


# create division function, return division sum
def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b


# create multiply function, return multiple sum
def multiple(a, b):
    print(f"MULTIPLE {a} * {b}")
    return a * b


numberOne = input("Enter a number: ")
numberTwo = input("Enter another number: ")
result = float(numberOne), float(numberTwo)

print(result)
