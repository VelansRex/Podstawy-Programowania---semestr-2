# 53. Write a Python program to find the first repeated character in a given string.

def powtorzenie(string):
    for index, c in enumerate(string):
        if string[:index+1].count(c) > 1:
            return c

    return "None"

print(powtorzenie("bcdabcd"))
print(powtorzenie("abcd"))