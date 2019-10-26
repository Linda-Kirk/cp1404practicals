import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')
    print("Changed directory is: {}".format(os.getcwd()))
    # filename = 'chords.docxz'
    # file_extension = filename.split('.')[-1]
    # print(filename)
    # print(file_extension)

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]

        try:
            os.mkdir(file_extension)
            print("New folder: ", file_extension)
        except FileExistsError:
            print("Folder already exists:", file_extension)
            pass

        print("Moving {} to {}/{}".format(filename, file_extension, filename))
        shutil.move(filename, "{}/{}".format(file_extension, filename))

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))


main()
