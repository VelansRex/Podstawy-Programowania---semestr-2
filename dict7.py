# 9. Write a Python program to iterate over dictionaries using for loops.

# Create a dictionary 'd' with color names as keys and corresponding numerical values as values.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

# Iterate through the key-value pairs in the dictionary 'd' using a for loop.
for color_key, value in d.items():
    # Print the color name, 'corresponds to', and its corresponding numerical value.
    print(color_key, 'corresponds to ', d[color_key])