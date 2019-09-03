"""
CP1404/CP5632 Practical
Word Occurrences
"""

user_string = input('Text: ')
words = user_string.split()
print(words)
words_dictionary = {}
for word in words:
    count_of_word = words_dictionary.get(word, 0)
    if count_of_word is None:
        words_dictionary[word] = 1
    else:
        words_dictionary[word] = count_of_word + 1

for word in words_dictionary:
    print("{} : {}".format(word, words_dictionary[word]))


print(words_dictionary)

