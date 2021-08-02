import random

minimum = 1
maximum = 10

answer = random.randint(minimum,maximum)
guess = 0
counter = 0

while guess != answer and counter != 3:
    guess = int(input('Guess a number: '))
    if guess == answer:
        print('Congratulation!! your answer is correct!!')
    elif guess < answer:
        print('your number is too small')
        counter += 1
    elif guess > answer:
        print('your number is too big')
        counter += 1

if counter == 3:
    print('you lose!')
