def main():
    my_string = input("Enter String: ")

    def count_letters(text):
        letter_count = 0
        for char in text:
            if char.isalpha():
                letter_count += 1
        return letter_count

    count_of_letters = count_letters(my_string)
    print("There are {} letters in the string {}".format(count_of_letters, my_string))


main()
