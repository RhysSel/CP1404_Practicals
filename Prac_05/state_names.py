
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT":
                   "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state.ljust(3), "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
for abbreviation in STATE_NAMES:
    print("{:3} is {}".format(abbreviation,STATE_NAMES[abbreviation]))
