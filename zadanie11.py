# 24. Write a Python program to check whether a string starts with specified characters.

def checking(string, letter):
        return string.startswith(letter)

print(checking("Hello", "He"))
print(checking("Paweł", "D"))