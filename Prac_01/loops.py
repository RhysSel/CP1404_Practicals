for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 1, -1):
    print(i, end=' ')
print()

stars = int(input("Number of stars: "))
for i in range(stars):
    print('*', end=' ')
print()

for i in range(stars):
    print('*' * (i + 1), end=' ')
    print()
