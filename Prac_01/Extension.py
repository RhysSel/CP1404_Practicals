Price = float(input('What is the price per kWh in cents? '))
Usage = float(input('What is your daily usage in kWh? '))
Billing_days = float(input('How many days are in your billing period? '))

if Price > 0 and Usage > 0 and Billing_days > 0:
    Total_cost = Price * Usage * Billing_days / 100
    print('Your estimated bill is $', Total_cost)
else:
    if Price <= 0 or Usage <= 0 or Billing_days <= 0:
        print('Input a valid number pleb')