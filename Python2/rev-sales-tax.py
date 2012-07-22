#!/usr/bin/env python2

# Getting a rough estimate of the sales tax rate of a purchase.
# Assumes a purchase where everything is taxable.

# How much did you pay?
total = float(raw_input("What was your total: "))

# How much was the tax?
tax = float(raw_input("How much was tax: "))

# Do math, print tax rate
print "You paid about a", round(tax / (total - tax) * 100, 3), '% tax rate.'

# Wait for user to press enter
raw_input("Press ENTER to exit")
