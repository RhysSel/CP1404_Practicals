

HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#ffefdb",
               "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
               "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
               "aquamarine1": "#7fffd4","aquamarine2": "#76eec6",
               "aquamarine4": "#458b74",}
# print(STATE_NAMES)

colour = input("Enter name of hex colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print(colour.ljust(3), "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name ").lower()
