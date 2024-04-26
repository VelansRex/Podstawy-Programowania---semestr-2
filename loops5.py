# 5. Write a  Python program that accepts a word from the user and reverses it.

# Prompt the user to input a word
word = input("Input a word to reverse: ")

# Iterate through the characters of the word in reverse order
for char in range(len(word) - 1, -1, -1):
    # Print each character from the word in reverse order without a new line (end="")
    print(word[char], end="")

# Print a new line to separate the reversed word from the next output
print("\n")