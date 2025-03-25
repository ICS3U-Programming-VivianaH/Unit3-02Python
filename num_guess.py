#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 25 2025
# This program asks the user to guess a number between 0 and 9
# Set correct number
CORRECT_NUMBER = 5

# Ask user for a guess
user_guess = int(input("Guess a number between 0 and 9: "))

# Check if the guess is correct
if user_guess == CORRECT_NUMBER:
    print("You guessed correctly!")

# Check if the guess is incorrect
if user_guess != CORRECT_NUMBER:
    print("You guessed wrong")
