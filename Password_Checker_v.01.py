# Modules


import time


# Start


print('Password must be at least 8 characters.')


# Password entering and length control


while True:
    password = input('Password: ')

    # Check if password is at least 8 characters long
    if len(password) < 8:
        print('Password must be at least 8 characters!')
        continue
    else:
        break


# Re-entering password for verification


while True:
    print('Please re-enter your password.')
    password_check = input('Password: ')

    if password_check != password:
        print('Incorrect password, please try again.')
        continue
    else:
        print('Correct password.')
        break




