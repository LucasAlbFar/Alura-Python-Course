import random

def play():
    print(' ')
    print('+++++++++++++++++++++++++++++')
    print('Welcome to the Guessing Game!')
    print('+++++++++++++++++++++++++++++')

    secret_number = random.randrange(1,101)
    trys = 0
    score = 1000

    print('Choose your level:'                                                                                                                  )
    print('(1) Easy (2) Normal (3) Hard')

    level = int(input('Level: '))
    while (level < 1 or level > 3):
        level = int(input('Invalid Level! Try a level between 1 and 3: '))

    if (level == 1):
        trys = 20
    elif (level == 2):
        trys = 10
    else:
        trys = 5

    for counter in range(1,trys + 1):
        print('Round {} of {}'.format(counter,trys))
        guess = int(input("Insert a number: "))

        if (guess < 1 or guess > 100):
            print('Invalid guess. Try a number between 1 to 100')
            continue

        print("Your guess is",guess)

        well_done = guess == secret_number
        greater   = guess > secret_number
        smaller   = guess < secret_number

        if (well_done):
            print('Well Done :) {} points'.format(score))
            break
        else:
            if (greater):
                print('Bad luck :( Your guess is greater than the secret number!')
            elif (smaller):
                print('Bad luck :( Your guess is smaller than the secret number!')
            lost_points = abs(secret_number - guess)
            score = score - lost_points

if (__name__ == '__main__'):
    play()
