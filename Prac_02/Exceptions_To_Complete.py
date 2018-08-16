"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input('please put a valid number'))
        finished = True   # will close the while loop
    except:
        print("Please enter a valid integer.")
print("Valid result is:", result)