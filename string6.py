# 8. Write a Python function that takes a list of words and
# return the longest word and the length of the longest one.

def find_longest_word(words):
    word_list =[]

    for i in words:
        word_list.append((len(i), i))
    word_list.sort()

    return word_list[-1][0], word_list[-1][1]

result = find_longest_word(["Python", "C++", "Pascal", "Ruby", "Go"])

print(f"Longest word: {result[1]}")
print(f"Length of the longest word: {result[0]}")
