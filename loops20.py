# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number.

# Prompt the user to input a number and convert it to an integer, assigning it to the variable 'n'
n = int(input("Input a number: "))

# Use a for loop to iterate 10 times, starting from 1 up to 10 (excluding 11)
for i in range(1, 11):
    # Print the multiplication table for the entered number 'n' by multiplying it with each iteration 'i'
    print(n, 'x', i, '=', n * i)