# Simple Calculator Program

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main function to run the calculator
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Take user input for operation
    operation = input("Enter choice (1/2/3/4): ")

    # Take user input for two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    # Perform the chosen operation and display the result
    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation (1/2/3/4).")

# Run the calculator
if __name__ == "__main__":
    main()
