import re

# Regular expression pattern for basic email validation
email_pattern = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

# Get user input for email
user_email = input('Enter your Email - ')

# Compile the regular expression with the IGNORECASE flag
pattern = re.compile(email_pattern, re.IGNORECASE)

# Check if the entered email matches the pattern
if pattern.match(user_email):
    print('Correct Email')
else:
    print('Wrong Email')
