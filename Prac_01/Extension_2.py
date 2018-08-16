Name= str(input('What is your name?'))
Menu = '''(1) to say Hello
(2) to say Goodbye
(3) to Quit
'''

print('Hello ',Name ,'to use this program please click',Menu)

A= int(input('Please type one of these numbers'))
while A != 3:
    if A == 1:
        print('Hello ',Name)
        A = int(input('Please type one of these numbers'))
    elif A == 2:
        print('Goodbye ', Name)
        A = int(input('Please type one of these numbers'))
    else:
        print('Invalid input please try again')
        print(Menu)
        A = int(input('Please type one of these numbers'))