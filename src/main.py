# Resolve the problem!!
import random
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
#ASCII = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')


def generate_password():
    # Start coding here
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbol = string.punctuation
    
    #letters = string.ascii_letters + string.digits + string.punctuation
    password = ( 
        ''.join(random.choice(upper) for i in range(random.randint(2,4))) +
        ''.join(random.choice(lower) for i in range(random.randint(2,4))) +
        ''.join(random.choice(digits) for i in range(random.randint(2,4))) +
        ''.join(random.choice(symbol) for i in range(random.randint(2,4)))
    )
    print(password) 
    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
