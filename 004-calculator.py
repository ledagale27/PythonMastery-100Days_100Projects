#!/usr/bin/env python3

#Simple Calculator

#Step 1: Get user input for two numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

#Step 2: Perform arithmetic operation
addition = number_1 + number_2
substraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2 if number_2 != 0 else "Cannot divide by zero"

#Step 3: Display the results
print("\n --- Calculator Results ---")
print(f'Addition: {number_1} + {number_2} = {addition}')
print(f'Substraction: {number_1} - {number_2} = {substraction}')
print(f'Multiplication: {number_1} x {number_2} = {multiplication}')
print(f'Division: {number_1} / {number_2} = {division}')
