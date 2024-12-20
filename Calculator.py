def simple_calculator():
    while True:  # Loop until valid input is received
        # Display the menu of operations
        print("Simple Calculator")
        print("Choose an operation:")
        print("A. Add")
        print("S. Subtract")
        print("M. Multiply")
        print("D. Divide")

        # Prompt the user to select an operation
        operation = input("Enter the operation (A/S/M/D): ").upper()  # Convert to uppercase for case-insensitivity

        # Validate the operation input
        if operation not in ['A', 'S', 'M', 'D']:
            print("Invalid input! Please select A, S, M, or D.")
            continue  # Keep asking for a valid operation

        # Prompt the user to input two numbers
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                break  # Break out of the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        # Perform the selected operation using if-elif-else
        if operation == 'A':  # Addition
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == 'S':  # Subtraction
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == 'M':  # Multiplication
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == 'D':  # Division
            # Check for division by zero
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")

        # Ask the user if they want to perform another operation
        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break  # Exit the loop if the user doesn't want to continue


# Run the calculator
simple_calculator()
