# 15. Write a Python program to get the maximum and minimum values of a dictionary.

# Create a dictionary 'my_dict' with key-value pairs.
my_dict = {'x': 500, 'y': 5874, 'z': 560}

# Find the key with the maximum value in 'my_dict' using the 'max' function and a lambda function.
# The 'key' argument specifies how the maximum value is determined.
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))

# Find the key with the minimum value in 'my_dict' using the 'min' function and a lambda function.
# The 'key' argument specifies how the minimum value is determined.
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# Print the maximum value by using the 'key_max' to access the corresponding value in 'my_dict'.
print('Maximum Value: ', my_dict[key_max])

# Print the minimum value by using the 'key_min' to access the corresponding value in 'my_dict'.
print('Minimum Value: ', my_dict[key_min])