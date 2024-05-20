def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    print("Welcome to the Simple Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
        operator = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif operation == '4':
        result = divide(num1, num2)
        operator = '/'
    else:
        print("Invalid operation choice!")
        return

    print(f"\nThe result of {num1} {operator} {num2} is: {result}")

if __name__ == "__main__":
    main()
