import math
import sys

history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        print("Error: Cannot take square root of negative number.")
        return None
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    return math.factorial(x)

def logarithm(x, base=10):
    if x <= 0:
        print("Error: Logarithm undefined for zero or negative numbers.")
        return None
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    try:
        return math.tan(math.radians(x))
    except:
        print("Error: Undefined tangent value.")
        return None

def show_history():
    if not history:
        print("No calculations yet.")
        return
    print("\nCalculation History:")
    for i, record in enumerate(history, 1):
        print(f"{i}. {record}")
    print()

def calculator_menu():
    while True:
        print("Advanced Python Calculator")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exponent (^)")
        print("6. Square Root (√)")
        print("7. Factorial (!)")
        print("8. Logarithm (log)")
        print("9. Sine (sin)")
        print("10. Cosine (cos)")
        print("11. Tangent (tan)")
        print("12. Show History")
        print("13. Exit")

        choice = input("Select an option (1-13): ")

        if choice in [str(i) for i in range(1, 12)]:
            if choice in ['6', '7', '8', '9', '10', '11']:
                try:
                    num = float(input("Enter the number: "))
                except ValueError:
                    print("Invalid input. Enter a number.")
                    continue

                if choice == '6':
                    result = square_root(num)
                    operation = f"√{num} = {result}"
                elif choice == '7':
                    result = factorial(int(num))
                    operation = f"{int(num)}! = {result}"
                elif choice == '8':
                    base_input = input("Enter logarithm base (default 10): ")
                    base = float(base_input) if base_input else 10
                    result = logarithm(num, base)
                    operation = f"log base {base} of {num} = {result}"
                elif choice == '9':
                    result = sin(num)
                    operation = f"sin({num}) = {result}"
                elif choice == '10':
                    result = cos(num)
                    operation = f"cos({num}) = {result}"
                elif choice == '11':
                    result = tan(num)
                    operation = f"tan({num}) = {result}"

            else:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Enter a number.")
                    continue

                if choice == '1':
                    result = add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"
                elif choice == '4':
                    result = divide(num1, num2)
                    if result is None:
                        continue
                    operation = f"{num1} / {num2} = {result}"
                elif choice == '5':
                    result = exponent(num1, num2)
                    operation = f"{num1} ^ {num2} = {result}"

            print(f"Result: {result}\n")
            history.append(operation)

        elif choice == '12':
            show_history()
        elif choice == '13':
            print("Exiting calculator. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    calculator_menu()
