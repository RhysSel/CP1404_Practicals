import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many lines of quick picks do you want? "))
    while number_of_quick_picks < 0:
        print('Please enter a valid value')
        number_of_quick_picks = int(input("How many lines of quick picks do you want? "))

    for i in range(number_of_quick_picks):
        quick_pick_list = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick_list:
                    number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick_list.append(number) #adds new number to list
        quick_pick_list.sort()  # sorts based on numeric value low to high
        print(" ".join("{:2}".format(number) for number in quick_pick_list))


main()
