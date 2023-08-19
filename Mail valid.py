import re
emailcheck = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
useremail = input('Enter your Email - ')

if re.search(emailcheck,useremail):
    print('Correct Email')
else:
    print('Wrong Email')
