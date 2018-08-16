sales = float(input("Enter sales: $"))
a = 0.1
b = 0.15
# if sales < 0:
#     print('Invalid entry gimp')
# else:
#     if sales < 1000:
#         bonus = sales * a
#
#     if sales >= 1000:
#         bonus = sales * b
#         print(bonus)

while sales >= 0:
    if sales < 1000:
        bonus = sales * a
    else:
        bonus = sales * b
    print(bonus)
    sales = float(input("Enter sales: $"))
