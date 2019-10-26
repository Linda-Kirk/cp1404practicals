import shutil
import os


def main():
    """Create folders from user input and sort files on extension according to user preferences"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')
    print("Changed directory is: {}".format(os.getcwd()))

    # Create empty dictionary for file extensions and associated category
    file_extension_mapped_to_category = {}

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]

        if file_extension not in file_extension_mapped_to_category:
            category = input("What category would you like to sort {} files into? ".format(file_extension))
            file_extension_mapped_to_category[file_extension] = category

            try:
                os.mkdir(category)
                print("New folder: ", category)
            except FileExistsError:
                print("Folder already exists:", category)
                pass

        print("Moving {} to {}/{}".format(filename, category, filename))
        # print("Moving {} to {}/{}".format(filename, file_extension_mapped_to_category[file_extension], filename))
        shutil.move(filename, "{}/{}".format(category, filename))

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))


main()
