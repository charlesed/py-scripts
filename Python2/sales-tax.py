#!/usr/bin/env python2

# Calculating some sales tax...

# What's your tax rate? 
tax_percentage = float(raw_input("Tax rate(%): "))
tax_rate = tax_percentage / 100

# Now what's your price?
subtotal = float(raw_input("Subtotal: "))

# Do some math and print the total
print round(subtotal + (subtotal * tax_rate), 2)

# Wait for user to press enter
raw_input("Press ENTER to exit")
