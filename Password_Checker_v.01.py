# Start

import time

print('Password must be at least 8 letters.')

# Password Entering And Loop

while True:
    password = input('Password: ')

# Password 8 Characters Long Control


    if len(password) < 8:
        print('Password must be at least 8 characters!')
        continue
    elif len(password) > 8 or len(password) == 8:
        break
        condition_1 = False

# Re-Entering Password


while True:
    print('Please re-enter your password.')
    password_check = input('Password: ')

    if password_check != password:
       print('Incorrect password please try again.')

       continue


    elif password_check == password:
        print('Correct password.')
        condition_2 = False
        break



