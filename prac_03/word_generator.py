"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    valid_input = False
    while not valid_input:
        word_format = input("Enter the word format e.g. 'ccvcvvc'(c for consonants, v for vowels):").lower()
        valid_input = is_valid_format(word_format)

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format(word_format):
    for char in word_format:
        if char not in "cv":
            print("Invalid character")
            return False
    else:
        return True


main()
