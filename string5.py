# 7. Write a Python program to find the first appearance
# of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.

def not_poor(string1):
    snot = string1.find('not')

    spoor = string1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        string1 = string1.replace(string1[snot:(spoor+4)], 'good')
        return string1
    else:
        return string1

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))