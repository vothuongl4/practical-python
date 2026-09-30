# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment =1000
extra_month=12
total_paid = 0.0
total_month=0

while principal > 0:
    if extra_month > 0:
        principal = principal * (1 +rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        extra_month = extra_month - 1
    else:
        principal = principal * (1 +rate/12) - payment
        total_paid = total_paid + payment
    total_month += 1

print("Total paid", total_paid)
print("Total mounth", total_month)