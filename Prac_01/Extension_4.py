Name = str(input('What is your name?'))
x = int(input('What number would you like x to be?'))
y = int(input('What number would you like y to be?'))
Menu = '''
(1) Show the even numbers from x to y
(2) Show the odd numbers from x to y
(3) Show the squares from x to y
(4) To quit
'''

print('Hello ',Name ,'to use this program please click ',Menu)

A = int(input('Please type one of these numbers'))
while A != 4:
    if A == 1:
        if x % 2 == 0: # even numbers from x to y
            for i in range(x,y,2):
                print(i)

        elif x % 2 != 0: #if x odd change to even
            x=x+1
            for i in range(x,y,2):
                print(i)
    elif A==2:               #Odd Numbers from x to Y
         if x % 2 != 0:
            for i in range(x, y, 2):
                print(i)

         elif x % 2 == 0: #if x even change it to odd
            x=x+1
            for i in range(x, y, 2):
                print(i)
    elif A==3:
        pass

    else:
        print('Invalid input please try again')
        print(Menu)
        A = int(input('Please type one of these numbers'))

