# use caps to create variables
# Can't have both ways either it has to be a int or string fool
LOWER_BOUNDARY = 33
UPPER_BOUNDARY = 127
MAX_COLUMNS = 10
MIN_COLUMNS = 2

""""
char = input('Please input a character')
print('The ASCII code for {},is {}'.format(char,ord(char)))

number = int(input('Please input a number  between {} and {}'.format(LOWER_BOUNDARY,UPPER_BOUNDARY)))
while number > LOWER_BOUNDARY  and number < UPPER_BOUNDARY:
    print('The representative character for {} ASCII code is {}'.format(number,chr(number)))
    number = int(input('Please input a number  between {} and {}'.format(LOWER_BOUNDARY, UPPER_BOUNDARY)))
# ASCII table (single column)
"""""
"""""
char = input('Please input a character')
for value in range(LOWER_BOUNDARY, UPPER_BOUNDARY + 1): #add 1 as range stops 1 before boundary
    print("{:1} {:2}".format(char, ord(char))) #redo this is with the number for an actual table list
"""""
# We want columns of the same thing done previously

Column = int(input("Please enter between {} and {} columns".format(MIN_COLUMNS, MAX_COLUMNS)))
while Column < MIN_COLUMNS or Column > MAX_COLUMNS:
    print('Please use a proper amount of colums dingus')
    Column = int("Please enter between {} and {} colums".format(MIN_COLUMNS,
                                                                MAX_COLUMNS))  # this will allow for a proper value to be entered
# Work out how many rows are needed to fill data
Rows = int((UPPER_BOUNDARY + 1 - LOWER_BOUNDARY) / (Column))
# Use statement like a for this
x = LOWER_BOUNDARY
for rows in range(Rows + 1):
    for column in range(Column):
        print("{:2}{:6}".format(chr(x), x))
        x += 1
