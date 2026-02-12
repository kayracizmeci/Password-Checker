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


# Password enter (create password)


def password_enter():
    # Password Function
    for i in range(3):
        password_input = input('Password: ')

        # Length Control
        if len(password_input) < 8:
            print('Password must be at least 8 characters!')
            continue

        # Number Control
        if not any(character.isdigit() for character in password_input):
            print('You must include at least 1 number in your password!')
            continue

        # Special Character Control
        if not any(ch in special_characters for ch in password_input):
            print('You must include at least 1 special character in your password!')
            continue

        return password_input

    print('Too many failed attempts.')
    print('Program closing...')
    time.sleep(2)
    raise SystemExit


# Re-Entering Password Function


def password_check(password):

    for i in range(3):
        print('Please re-enter your password.')
        re_entered = input('Password: ')

        if re_entered != password:
            print('Incorrect password, please try again.')
            continue

        print('Correct password.')
        return True

    print('Too many incorrect attempts. Program locked.')
    raise SystemExit



password = password_enter()
password_check(password)
