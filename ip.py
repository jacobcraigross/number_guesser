# number guessing game with logic that will allow player to drill down to the answer.

import random

highest = 100
answer = random.randint(1, highest)

print('please guess a number between 1 and {}: '.format(highest))

# initialize to any number outside the given range of 1 to 10
guess = 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print('please guess higher')
    elif guess > answer:
        print('please guess lower')
    else:
        print('well done!')

        






