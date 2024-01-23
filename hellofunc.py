import random

print('try guess my number')
number = 13
guess = int(input())
while guess != number:
    if guess < number:
        print('is less than')
        guess = int(input())
        continue
    elif guess > number:
        print('is higher')
        guess = int(input())
        continue
print('correct')
