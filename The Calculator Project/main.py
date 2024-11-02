from art import logo
def add(a, b):
    return a + b

# TODO : Write out the other 3 functions (sub, mult, div)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# TODO : Add this 4 functions into a dict as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# TODO : Use the dict operations to perform the calculations. Multiply 4 * 8 using the dict

# print(operations["*"](4,8))
def calculator():
    print(logo)
    shouldAccumulate = True
    num1 = float(input("What is the first number?: "))

    while shouldAccumulate:
        for symbol in operations:
            print(symbol)
        operationSymbol = input("What operation would you like?: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operationSymbol](num1, num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'no' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        elif choice == "no":
            shouldAccumulate = False
            print("\n" * 20)
            calculator()

calculator()


