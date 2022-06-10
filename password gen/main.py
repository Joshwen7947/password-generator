import random

print(f'Welcome to the Password Generator')
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890/?.,<>:;'
# 
number = int(input("How many passwords do you need? "))
length = int(input("How long would you like your passwords? "))
# 
print(f'\nHere are your passwords: ')

for password in range(number):
    passwords = ''
    for chars in range(length):
        passwords += random.choice(char)
    print(passwords)


