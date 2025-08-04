#!/usr/bin/env python3

#Welcome Message Generator

#Step 1: Ask for user details
name = input("What's your name?")
hobby = input("What's your favourite hobby?")

#Step 2: Generate a personalized welcome message with the details given
print("\n --- Welcome Message ---")
print("Hello,{name} !".format(name =name))
print(f"Welcome to the world of Python Programming.")
print(f"It's great to know that you love {hobby}.")
print(f"Get ready to build something amazing today.")


