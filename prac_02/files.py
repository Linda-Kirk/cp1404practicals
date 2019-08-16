"""
This program asks user for their name and writes it to a file
"""

# Programme 1 Get name from user and write to file
name = input("Please enter your name: ")
out_file = open('data.txt', 'w')
print(name, file=out_file)
out_file.close()

# Programme 2 Read and Print name from file
in_file = open('data.txt', 'r')
name = in_file.read()
in_file.close()
print("Your name is {}".format(name))

# Programme 3 Create file and           This commented out as tutor asked that txt file be created independently
# out_file = open('numbers.txt', 'w')
# number_1 = 17
# number_2 = 42
# print(number_1, file=out_file)
# print(number_2, file=out_file)
# out_file.close()
in_file = open('numbers.txt', 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
result = number_1 + number_2
print("The result is :", result)

# Programme 4 Read and print multiple lines
in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print("The total is: {}".format(total))






