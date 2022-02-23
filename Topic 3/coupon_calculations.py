"""
Program: coupon_calculator.py
Author: Patricia Hernandez-Vasquez
Last date modified: 02/23/2022
The purpose of this program is to prompt the user for the amount of the purchase, the cash coupon, and the percent coupon.
The output should be the calculation of the three inputs.
"""
# set constant of tax
TAX = 6

# hardcode a price or get from user input; set to a variable
item_cost = float(input('Enter total cost of your purchase: $'))

# get coupon information from user input; set to a variable
cash_coupon = float(input('Enter amount of cash-off coupons: $'))
percent_coupon = int(input('Enter amount of percent discount coupons: '))

# part or step 1
# if cash_coupon then, do calculation
if cash_coupon == 5:
    after_cash_coupon = item_cost - 5
elif cash_coupon == 10:
    after_cash_coupon = item_cost - 10

# set a post cash coupon total variable (price after coupon)
# after_cash_coupon = item_cost - cash_coupon

# add a print statement here while you are working on it or debugging
# print(after_cash_coupon)

# part or step 2
# if percent_coupon then, do calculation
if percent_coupon == 10:
    (10 / 100) * after_cash_coupon

# set a discount percent amount
discount_percent_amount = (percent_coupon / 100) * after_cash_coupon

# set a post percent coupon total variable (Discount % amt)
post_percent_coupon = after_cash_coupon - discount_percent_amount

# to see result so far, add temporary print statement
# print(post_percent_coupon)

# Third step is to do tax (tax rate is below docstring)
tax_price = post_percent_coupon * (TAX / 100)

# set to a subtotal
subtotal = post_percent_coupon + tax_price

# to see result so far, add temporary print statement
# print(subtotal)

# Fourth is shipping (nested if statements)
# if the subtotal is less than 10, charge X amount for shipping
# etc...
if subtotal < 50.00:
    if subtotal < 10.00:
        shipping_rate = 5.95
    elif 10.00 <= subtotal < 30.00:
        shipping_rate = 7.95
    elif 30.00 <= subtotal < 50.00:
        shipping_rate = 11.95
else:
    shipping_rate = 0.00

total_price = int(subtotal + shipping_rate)

# to see result so far, add temporary print statement
# print(shipping_rate)

# to see result so far, add temporary print statement
# print(total_price)

# print out the total in a 'pretty' format
print(f'Your total: ${total_price: 5.2f}')
