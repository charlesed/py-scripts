#!/usr/bin/env python2

# Calculating some sales tax...

# What's your tax rate? 
tax = float(input("Tax rate(%): "))
tax = tax / 100

# Now what's your price?
price = float(input("Price: "))

# Do some math and print the total
tax = price * tax
total = price + round(tax, 2)
print(total)

# Wait for user to press enter
input("Press ENTER to exit")
