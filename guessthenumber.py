import random

print('Hello. What is your name?')
name = input()
randNum = random.randint(1, 10)
print(f'Hi, {name}, I am thinking of a number between 1 and 10.')

try:
    for i in range(1, 6):
        guess = int(input('Take a guess: '))
        if guess < randNum:
            print('Your guess is too low.')
        elif guess > randNum:
            print('Your guess is too high.')
        else:
            break
    if guess == randNum:
        print(f'Good job, {name}! You guessed my number in {i} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {randNum}')
except ValueError:
    print('Please enter a valid number')
    
