#!/usr/bin/python3
# Include the decimal module to use the Decimal type
from decimal import Decimal

# Define a float value
x = 3.14159265

# Use the format method to print the float with 2 decimal places
print("{:.2f}".format(x))

# Use the Decimal type to print the float with 4 decimal places
print("{:.4f}".format(Decimal(x)))
