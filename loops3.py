# 3. Write a Python program to guess a number between 1 and 9.

# Import the 'random' module to generate random numbers
import random

# Generate a random number between 1 and 10 (inclusive) as the target number
target_num, guess_num = random.randint(1, 10), 0

# Start a loop that continues until the guessed number matches the target number
while target_num != guess_num:
    # Prompt the user to input a number between 1 and 10 and convert it to an integer
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

# Print a message indicating successful guessing once the correct number is guessed
print('Well guessed!')