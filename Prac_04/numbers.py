MAX_NUMBERS = 5
numbers_list = []
for amount_of_numbers in range(0,MAX_NUMBERS,1):
    number = int(input('Please input a number'))
    numbers_list.append(number)

print(numbers_list)
print('The first number is ',numbers_list[0])
print('The last number is',numbers_list[-0])
print('The smallest number is',min(numbers_list))
print('The largest number is',max(numbers_list))
print('The average of the numbers is',sum(numbers_list)/len(numbers_list))