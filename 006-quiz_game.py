#!/usr/bin/env python3
#Basic Math Quiz game

import random

#Step 1: Define the math question function
def generate_question():
    number_1 = random.randint(1,10)
    number_2 = random.randint(1,10)
    operator = random.choice(["+","-","*"])

    if operator == "+":
        answer = number_1 + number_2
    elif operator == "-":
        answer = number_1 - number_2
    else:
        answer = number_1 * number_2

    return f'{number_1} {operator} {number_2}', answer

#Step 2: Define the main game function math_quiz()
def math_quiz():
    score = 0
    rounds = 5

    print("\n ---Welcome to the Math Quiz Game---")
    print("You will be presented with math problems, and you need to provide the correct answers")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1 
        else:
            print(f'Wrong! The correct answer is: {correct_answer}')
        
    print("\n---Game Over!---")
    print(f'Your final score is: {score}/{rounds}')

    if score == rounds:
        print("Congratulatios! You got all the questions correct.!")
    elif score >= rounds // 2:
        print("Good job! You did well.!")
    else:
        print("Keep practicing! You can do better next time.!")

#Step 3: Run the game math_quiz() function
math_quiz()
   