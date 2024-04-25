# 11. Write a Python program to multiply all the items in a dictionary.

# Create a dictionary 'my_dict' with keys 'data1', 'data2', and 'data3', along with their respective values.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

# Initialize a variable 'result' to 1. This variable will store the product of all values in the dictionary.
result = 1

# Iterate through the keys in the 'my_dict' using a for loop.
for key in my_dict:
    # Multiply the current 'result' by the value associated with the current key in 'my_dict'.
    result = result * my_dict[key]

# Print the final 'result,' which is the product of all values in the dictionary.
print(result)