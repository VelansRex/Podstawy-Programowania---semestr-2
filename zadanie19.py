#72. Write a Python program to remove all characters except a specified character from a given string.

# Function to remove all chars except given char
def remove_characters(str1,c):

  # List comprehension to keep only given char
  return ''.join([el for el in str1 if el == c])

# Test string
text = "Python Exercises"

# Print original string
print("Original string")
print(text)

# Character to keep
except_char = "P"

# Print message and result
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))

# Second test string
text = "google"
print("\nOriginal string")
print(text)

except_char = "g"

# Print message and result
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))

# Third test string
text = "exercises"
print("\nOriginal string")
print(text)

except_char = "e"

# Print message and result
print("Remove all characters except",except_char,"in the said string:")
print(remove_characters(text,except_char))