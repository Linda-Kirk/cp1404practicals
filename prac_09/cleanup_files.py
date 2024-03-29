"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


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


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            path_and_name = os.path.join(directory_name, filename)
            # print(path_and_name)
            path_and_new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(path_and_name, path_and_new_name))
            # os.rename(path_and_name, path_and_new_name)


# main()
demo_walk()
