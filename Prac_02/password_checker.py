"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
SPECIAL_CHARS_REQUIRED = False


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    x = 0
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    elif password.islower():
        return False
    elif password.isupper():
        return False
    elif password.isdigit():  # THIS ONLY EVALUATES ONE DIGIT
        return False
    elif x == 0:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                x += 1
                if x > 0:
                    return True


main()
