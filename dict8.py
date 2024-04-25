# 10. Write a Python program to sum all the items in a dictionary.

# Create a dictionary 'my_dict' with key-value pairs.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
# Use the 'sum' function to calculate the sum of all values in the 'my_dict' dictionary.
# 'my_dict.values()' extracts the values from the dictionary, and 'sum' calculates their sum.
result = sum(my_dict.values())
# Print the result, which is the sum of the values.
print(result)