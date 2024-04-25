# 25. Write a  Python program to print a dictionary in table format.

# Create a dictionary 'my_dict' with keys as 'C1', 'C2', and 'C3', and corresponding lists of values.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

# Use a list comprehension to create a list of tuples where each tuple contains a key and its corresponding list of values.
# Sort the items (key-value pairs) in the 'my_dict' dictionary based on their keys.
# The 'zip' function is used to transpose the rows and columns.
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # Print each row of transposed data as space-separated values.
    print(*row)