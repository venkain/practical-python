# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

month = 0
while principal > 0:
    month += 1
    if principal <= payment:
        payment = principal
        principal = 0
    else:
        principal = round(principal * (1+rate/12) - payment, 2)
    if extra_payment_start_month <= month < extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    total_paid = round(total_paid + payment, 2)
    print(month, total_paid, principal)

print('Total paid',total_paid)
print('Months', month)
