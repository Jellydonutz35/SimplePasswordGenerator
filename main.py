import random
from colorama import init
from colorama import Fore, Back, Style
chars = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+-="

while 1:
    password_len = int(input('Password Length: '))
    if password_len >= 50:
        print('ERROR!! To many Characters')
        password_len = int(input( 'Password Length: '))
    password_count = int(input('Amount of Passwords:'))
    for x in range(0, password_count):
        password = ""
        password_incr = x + 1
        for x in range(password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print('Password',password_incr,':',password)


