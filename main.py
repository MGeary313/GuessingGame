import random

number = random.randint(1, 100)

while number < 1 or number > 100:
    print('Please enter a number between 1 and 100')
    number = int(input())

print('Guess a number between 1 and 100')
guess = int(input())

while guess != number:
    if guess < number:
        guess = int(input('That guess is too low. Try again: '))
    elif guess > number:
        guess = int(input('That guess is too high. Try again: '))

if guess == number:
    print('Thats correct!')
