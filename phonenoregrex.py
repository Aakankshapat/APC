
import re

phone = input("Enter phone number: ")

pattern = r'^[6-9][0-9]{9}$'

if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")