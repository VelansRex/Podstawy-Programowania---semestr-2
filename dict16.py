# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

# Import the 'nlargest' function from the 'heapq' module.
from heapq import nlargest

# Create a dictionary 'my_dict' with key-value pairs.
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Use the 'nlargest' function to find the three largest keys in the 'my_dict' dictionary based on their values.
# The 'key' argument specifies that the values should be used for comparison.
three_largest = nlargest(3, my_dict, key=my_dict.get)

# Print the three largest keys found in the 'my_dict' dictionary.
print(three_largest)