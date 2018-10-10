from Prac_08.unreliable_car import UnreliableCar


def main():

    reliable_car = UnreliableCar("Great", 100, 90)
    terrible_car = UnreliableCar("Shoddy", 100, 9)

    for i in range(1, 6):
        print("{:7} drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:7} drove {:2}km".format(terrible_car.name, terrible_car.drive(i)))

    print(reliable_car)
    print(terrible_car)
main()