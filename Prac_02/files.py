# Program 1
name = str(input('what is your name? '))
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# Program 2
file = open('name.txt', "r")
for line in file:
    print(line)
out_file.close()

# Program 3
file = open('numbers.txt', 'r')
x = int(file.readline())
y = int(file.readline())
print(x + y)
out_file.close()

# Program 4
file = open('numbers.txt', 'r')
y = 0
for line in file:
    number = int(line)
    y += number
    print(y)
out_file.close()
