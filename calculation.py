

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0:
        return "Error! Logarithm base and argument must be positive."
    return math.log(x, base)

def calculation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Exit")
    print("")

def main():
    while True:
        calculation()
        choice = input("Enter choice (1-8): ")
        print("")

        if choice == '8':
            print("Exiting the calculator.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("")

            if choice == '1':
                
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"The result is: {square_root(num)}")

        elif choice == '7':
            num = float(input("Enter number: "))
            base = float(input("Enter logarithm base: "))
            print(f"The result is: {logarithm(num, base)}")

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()