# 47. Write a Python program to lowercase the first n characters in a string.

string = "PYTHON JEST ELEGANCKI!"

n = int(input("Ile liczb zmienić? "))

print(string[:n].lower() + string[n:])