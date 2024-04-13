# 21. Write a Python function to convert a given
# string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def to_uppercase(string):
    num_upper = 0

    for c in string[:4]:
        if c.upper() == c:
            num_upper += 1
    if num_upper >= 2:
        return string.upper()

    return string

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))