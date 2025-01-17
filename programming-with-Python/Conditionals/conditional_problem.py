# The price of a house is $1,000,000.00, if the buyer has good credit,
# then the down payment is 10%. Otherwise, the down payment is 20%.

# Solution

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")