
import re

password = input("Enter password: ")

pattern = r'^[A-Za-z0-9@#$]{8,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")