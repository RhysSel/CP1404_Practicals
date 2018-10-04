from Prac_06.guitar import Guitar


def run_example():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 96,
                                                      guitar.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
if __name__ == '__main__':
    run_example()