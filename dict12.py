# 14. Write a Python program to sort a given dictionary by key.

# Create a dictionary 'color_dict' with color names as keys and their corresponding color codes in hexadecimal format as values.
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

# Iterate through the keys of the 'color_dict' dictionary after sorting them in lexicographical order.
for key in sorted(color_dict):
    # Print each key-value pair where '%s' is a placeholder for the key and its associated color code.
    print("%s: %s" % (key, color_dict[key]))