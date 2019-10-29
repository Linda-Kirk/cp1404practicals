def main():
    filename = get_fixed_filename("ItIsWell (oh my soul).txt")
    print(filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    new_name = ""
    previous_character = ""
    for i, character in enumerate(filename):
        print(i, character)
        if character.isupper() and previous_character is not "":
            new_name += '_' + character
        else:
            new_name += character
        previous_character = character
    print("After Loop: ", new_name)
    new_name = new_name.title().replace(" ", "_").replace(".TXT", ".txt")
    print("After adjustments: ", new_name)
    return new_name


main()
