def string_both_ends(string1):
    if len(string1) < 2:
        return ''

    return string1[0:2] + string1[-2:]

print(string_both_ends('Programowanie'))
