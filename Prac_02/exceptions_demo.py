"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
if denominator != 0:
    fraction = numerator / denominator
    print(fraction)


print("Finished.")

# 1. Char Entered
# 2. When the denominator is 0
# 3. Using a if statement for when denominator != 0
