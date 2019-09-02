"""
CP1404/CP5632 Practical
Hexadecimal colour codes in a dictionary
"""

HEXADECIMAL_COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4",
                       "BLACK": "#000000", "BLUE1": "#0000ff", "GREEN1": "#00ff00", "HOTPINK": "#ff69b4",
                       "ORANGE1": "#ffa500", "RED1": "#ff0000", "PURPLE": "#a020f0"}
# print(len(HEXADECIMAL_COLOURS))

colour = input("Enter a colour name: ").upper()
while colour != "":
    if colour in HEXADECIMAL_COLOURS:
        print(colour, "is", HEXADECIMAL_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter a colour name: ").upper()
