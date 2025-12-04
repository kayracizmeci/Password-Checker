# Modules
import time


# Start
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+', '[', ']',
    '{', '}', ';', ':', ',', '.', '<', '>',
    '/', '?', '\\', '|', '~'
]


print('RULES:')
print('Password must be at least 8 characters.')
print('Password must include at least 1 number.')
print('Password must include 1 special character.')


# Password check
password = None  

for i in range(3):
    password_input = input('Password: ')

    # Length check
    if len(password_input) < 8:
        print('Password must be at least 8 characters!')
        continue

    # Number check
    elif not any(character.isdigit() for character in password_input):
        print('You must include at least 1 number in your password!')
        continue

    # Special character check
    elif not any(char in special_characters for char in password_input):
        print('You must include at least 1 special character in your password!')
        continue

    else:
        print('Password accepted.')
        password = password_input
        break

if password is None:
    print('Too many failed attempts.')
    print('Program closing...')
    time.sleep(2)
    exit()


# Re-entering password for verification
for i in range(3):
    print('Please re-enter your password.')
    password_check = input('Password: ')

    if password_check != password:
        print('Incorrect password, please try again.')
        continue
    else:
        print('Correct password.')
        break
else:
    
    print('Too many incorrect attempts. Program locked.')
    exit()