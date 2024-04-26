# 14. Write a Python program that accepts a string and calculates the number of digits and letters.

# Prompt the user to input a string and store it in the variable 's'
s = input("Input a string")

# Initialize variables 'd' (for counting digits) and 'l' (for counting letters) with values 0
d = l = 0

# Iterate through each character 'c' in the input string 's'
for c in s:
    # Check if the current character 'c' is a digit
    if c.isdigit():
        # If 'c' is a digit, increment the count of digits ('d')
        d = d + 1
    # Check if the current character 'c' is an alphabet letter
    elif c.isalpha():
        # If 'c' is an alphabet letter, increment the count of letters ('l')
        l = l + 1
    else:
        # If 'c' is neither a digit nor an alphabet letter, do nothing ('pass')
        pass

# Print the total count of letters ('l') and digits ('d') in the input string 's'
print("Letters", l)
print("Digits", d)