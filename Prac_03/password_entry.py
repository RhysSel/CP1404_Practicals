"""Rhys Selwyn"""
password = str(input('Please put word'))
if len(password) >= 6 or len(password) <= 3:
    print('Wrong passowrd')
    password = str(input('Please put word'))
elif len(password) < 6 and len(password) > 3:
    for i in range (len(password)):
        print('*',end='')