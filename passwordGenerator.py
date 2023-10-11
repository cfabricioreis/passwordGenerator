import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number_of_passwords = int(input ('Amount of passwords to generate: '))

password_length = int(input('Input your password length: '))

print ('\nHere are your passwords:')

for passw in range(number_of_passwords):
    password = ''
    for c in range(password_length):
        password += random.choice(chars)
    print (password)

