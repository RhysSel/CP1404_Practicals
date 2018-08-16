Total_cost = 0
item = int(input('How many items do you have today?'))
Cost = float(input('How much does each item cost?'))  # float to stop rounding up

while item <= 0:
    print('Put in a real number dingus')
    for i in range(item):
        Total_cost *= Cost
        print("The total cost of", item, 'items is equal to the total of $', Total_cost)

        if Total_cost > 100:
            Total_cost *= 0.9
            print("The total cost of", item, 'items is equal to the total of $', Total_cost)
