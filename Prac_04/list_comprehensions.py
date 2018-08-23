"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

number_string = ['0','1','2']



lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)


# greater than 9 from the numbers (not strings) you just created
big_numbers = [number for number in numbers if number > 9]
print(big_numbers)

number_from_string =[int(number_string) for number_string in number_string]
print(number_from_string)