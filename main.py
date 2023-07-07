import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def main():
    print("Welcome to the Scientific Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-10): ")

        if choice == '0':
            print("Thank you for using the Scientific Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '7']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        elif choice in ['6']:
            num1 = float(input("Enter a number: "))

        elif choice in ['8', '9', '10']:
            num1 = float(input("Enter an angle in degrees: "))
            num1 = math.radians(num1)

        if choice == '1':
            print("Result: ", add(num1, num2))

        elif choice == '2':
            print("Result: ", subtract(num1, num2))

        elif choice == '3':
            print("Result: ", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result: ", divide(num1, num2))

        elif choice == '5':
            print("Result: ", power(num1, num2))

        elif choice == '6':
            if num1 < 0:
                print("Error: Square root of a negative number is not allowed.")
            else:
                print("Result: ", square_root(num1))

        elif choice == '7':
            if num1 <= 0 or num2 <= 0:
                print("Error: Arguments must be positive for logarithm.")
            else:
                print("Result: ", logarithm(num1, num2))

        elif choice == '8':
            print("Result: ", sin(num1))

        elif choice == '9':
            print("Result: ", cos(num1))

        elif choice == '10':
            if math.cos(num1) == 0:
                print("Error: Tangent is undefined for 90 and 270 degrees.")
            else:
                print("Result: ", tan(num1))

        else:
            print("Invalid choice. Please enter a number between 0 and 10.")

        print("\n")

if __name__ == '__main__':
    main()








