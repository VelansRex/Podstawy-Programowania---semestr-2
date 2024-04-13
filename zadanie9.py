# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.

def first_three(string):
    if len(string) > 3:
        return string[:3]
    else:
        return string

print(first_three("ipy"))
print(first_three("Python"))
print(first_three("py"))
