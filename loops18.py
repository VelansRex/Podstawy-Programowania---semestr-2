# 40. Write a Python program to find the median of three values.

# Prompt the user to input the first number and convert it to a floating-point number, assigning it to the variable 'a'
a = float(input("Input first number: "))

# Prompt the user to input the second number and convert it to a floating-point number, assigning it to the variable 'b'
b = float(input("Input second number: "))

# Prompt the user to input the third number and convert it to a floating-point number, assigning it to the variable 'c'
c = float(input("Input third number: "))

# Determine the median among the three numbers

# Check if 'a' is greater than 'b'
if a > b:
    # Check if 'a' is less than 'c'
    if a < c:
        median = a
    # Check if 'b' is greater than 'c'
    elif b > c:
        median = b
    else:
        median = c
# If 'a' is not greater than 'b'
else:
    # Check if 'a' is greater than 'c'
    if a > c:
        median = a
    # Check if 'b' is less than 'c'
    elif b < c:
        median = b
    else:
        median = c

# Display the calculated median among the three input numbers
print("The median is", median)