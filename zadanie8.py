# 16. Write a Python function to insert a string in the middle of a string.

def insert_string_middle(string, middle_char):
    return string[:2] + middle_char + string[2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('<<>>', 'HTML'))