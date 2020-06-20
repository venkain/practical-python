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
    principal = principal * (1+rate/12) - payment
    if extra_payment_start_month <= month < extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    total_paid = total_paid + payment
    print(month, f'{total_paid:,.2f}', f'{principal:,.2f}')

print('Total paid',f'{total_paid:,.2f}')
print('Months', month)
