TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

Usage = float(input('What is your daily usage in kWh? '))

Billing_days = float(input('How many days are in your billing period? '))

Tariff = int(input('What tariff are you currently using? '))

if Tariff == 11:
    Total_cost = TARIFF_11 * Usage * Billing_days / 100
    print('Your estimated bill is $', Total_cost)

else:
    if Tariff == 31:
        Total_cost = TARIFF_31 * Usage * Billing_days / 100

    if Tariff != 31 or Tariff != 11 or Usage <= 0 or Billing_days <= 0:
        print('/n One of your entries is invalid please check to make sure')
        print('no values are 0 and the correct tarriff has been entered')
