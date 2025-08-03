#!/usr/bin/env python3

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        # Validate the choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid option. Try again.")
            continue

        # Get the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Perform calculation
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2

        # Show result
        print(f"Result: {result}")

# Run the calculator
calculator()
