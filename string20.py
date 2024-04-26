#73. Write a  Python program to count Uppercase, Lowercase, special characters and
# numeric values in a given string.

# Function to count character types
def count_chars(str):

  # Initialize counters
  upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0

  # Iterate through string
  for i in range(len(str)):

    # Increment appropriate counter
    if str[i] >= 'A' and str[i] <= 'Z':
      upper_ctr += 1
    elif str[i] >= 'a' and str[i] <= 'z':
      lower_ctr += 1
    elif str[i] >= '0' and str[i] <= '9':
      number_ctr += 1
    else:
      special_ctr += 1

  # Return all counters
  return upper_ctr, lower_ctr, number_ctr, special_ctr

# Test string
str = "@W3Resource.Com"

# Print original string
print("Original Substrings:",str)

# Call function and unpack counters
u, l, n, s = count_chars(str)

# Print counters
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)