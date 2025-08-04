#!/usr/bin/env python3

#Simple Calculator - Basic option 1

#Step 1: Get user input for two numbers
#number_1 = float(input("Enter the first number: "))
#number_2 = float(input("Enter the second number: "))

#Step 2: Perform arithmetic operation
#addition = number_1 + number_2
#substraction = number_1 - number_2
#multiplication = number_1 * number_2
#division = number_1 / number_2 if number_2 != 0 else "Cannot divide by zero"

#Step 3: Display the results
#print("\n --- Calculator Results ---")
#print(f'Addition: {number_1} + {number_2} = {addition}')
#print(f'Substraction: {number_1} - {number_2} = {substraction}')
#print(f'Multiplication: {number_1} x {number_2} = {multiplication}')
#print(f'Division: {number_1} / {number_2} = {division}')

#Calculator Option 2 calculator() functionS

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

        # Validate the choice given
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