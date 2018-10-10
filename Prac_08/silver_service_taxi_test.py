from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 50, 5)
    taxi.drive(11)
    print(taxi)
    print(taxi.get_fare())

main()