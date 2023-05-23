'''
hello, let's create a game of guessing random numbers. we will also tell if their guess is closer to the number. 
we will also tell how many guesses we have made.'''

import random

maxNum = input('Please the range of numbers you want to guess: ')

if maxNum.isdigit():
    maxNum = int(maxNum)
    if maxNum < 1:
        print('please enter a number higher than 0')
        exit()
else:
    print('please enter a number' )
    exit()

number = random.randint(1, maxNum)
totalGuesses = 0
while True:
    guess = int(input('guess a number: '))
    if guess == number:
        print('you guessed the number')
        totalGuesses += 1
        print(f'total guesses: {totalGuesses}')
        break
    elif guess > number:
        print('too high')
        totalGuesses += 1
        print(f'total guesses: {totalGuesses}')
        continue
    elif guess < number:
        print('too low')
        totalGuesses += 1
        print(f'total guesses: {totalGuesses}')
        continue