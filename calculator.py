# Basic Calculator in Python
# This program allows to perform simple arithmetic operations.

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract y from x"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide x by y (handles division by zero)"""
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

# Main program loop
while True:
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    # Get user choice
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop
    
    if choice in ('1', '2', '3', '4'):
        # Get the numbers from the user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers!")
            continue  # Skip to the next iteration
        
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice! Please select a valid option (1/2/3/4/5).")
