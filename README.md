# 🧮 Calculator Project 🧮

Welcome to the **Calculator Project**! This program provides a simple calculator functionality that supports **addition**, **subtraction**, **multiplication**, and **division** operations. The calculator allows users to perform multiple calculations in a single session.

## 🌟 Features

- **Basic Arithmetic Operations**: The calculator supports addition, subtraction, multiplication, and division.
- **Continuous Calculation**: After performing an operation, users can choose to continue calculating with the result or start a new calculation.

## 🎨 Logo

```plaintext
logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
```

## ⚙️ How It Works
  The program uses a dictionary to store operations as key-value pairs, where the keys are the operation symbols and the values are the corresponding functions.

## ➕ Operations Supported
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

## 📖 Example Usage
```bash
# To perform calculations, simply run the calculator function.
calculator()
```

## 💻 Code Snippet
```python
from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

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
```

## 🛠️ Requirements
  - Python 3.x

## 🎉 Conclusion
  Feel free to contribute to this project by adding new features or enhancing existing functionalities. Happy calculating! 🎉





