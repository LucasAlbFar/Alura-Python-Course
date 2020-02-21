print('+++++++++++++++++++++++++++++')
print('Welcome to the Guessing Game!')
print('+++++++++++++++++++++++++++++')

secret_number = 87
trys = 3

guess = int(input("Insert a number: "))
print("Your guess is",guess)

well_done = guess == secret_number
greater   = guess > secret_number
smaller   = guess < secret_number

if (well_done):
    print('Well Done :)')
else:
    if (greater):
        print('Bad luck :( Your guess is greater than the secret number!')
    elif (smaller):
        print('Bad luck :( Your guess is smaller than the secret number!')