# 24. Write a  Python program to create a dictionary from a string.

# Import the 'defaultdict' and 'Counter' classes from the 'collections' module.
from collections import defaultdict, Counter

# Create a string 'str1' containing characters.
str1 = 'w3resource'

# Create an empty dictionary 'my_dict' to store character counts.
my_dict = {}

# Iterate through the characters in the string 'str1' using a for loop.
for letter in str1:
    # Update the 'my_dict' by incrementing the count of the current character.
    # Use the 'get' method with a default value of 0 to initialize counts for new characters.
    my_dict[letter] = my_dict.get(letter, 0) + 1

# Print the 'my_dict' dictionary, which contains character counts.
print(my_dict)