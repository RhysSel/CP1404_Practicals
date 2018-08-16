def main():
    """Gets score , evaluates through other fnctn"""
    mark = float(input('Please input your total mark out of 100'))
    print(evaluate_mark(mark))


def evaluate_mark(mark):
    """ Evaluates the score given """
    if mark > 100 or mark < 0:
        return ''
    elif mark >= 85:
        return 'HD'
    elif mark >= 75:
        return 'D'
    elif mark >= 65:
        return 'Credit'
    elif mark >= 50:
        return "Pass"
    else:
        return 'N'


main()
