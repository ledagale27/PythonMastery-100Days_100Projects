#!/usr/bin/env python3

#Number comparison tool

#Step 1: Get user input for two numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

#Step 2: Compare the numbers given
print("\n ---Comparison results---")

if number_1 == number_2:
    print(f'Both numbers are equal: {number_1}')
elif number_1 > number_2:
    print(f'{number_1} is greater than {number_2}')
else:
    print(f'{number_2} is greater than {number_1}')

# Step 3: Check if any number is zero 
if number_1 == 0 or number_2 == 0:
    print(f'\n At least one number is zero')
else:
    print(f'\n Both numbers are non-zero')
