import random


def play():
    print_header()
    secret_word = load_secret_word()
    right_letters = init_right_letters(secret_word)

    print(right_letters)

    hanged = False
    matched = False
    mistakes = 0

    while (not hanged and not matched):
        guess = player_input()

        if (guess in secret_word):
            mark_correct_guess(secret_word,guess,right_letters)
        else:
            mistakes += 1
            draw_hang(mistakes)

        hanged = mistakes == 7
        matched = "__" not in right_letters
        print(right_letters)

    if (hanged):
        loser_message(secret_word)
    else:
        win_message()


def print_header():
    print(' ')
    print('+++++++++++++++++++++++++++++')
    print('Welcome to the Hangman Game!')
    print('+++++++++++++++++++++++++++++')

def load_secret_word():
    word_list = []
    with open("words.txt","r") as file:
        for line in file:
            word_list.append(line.strip())

    rand_position = random.randrange(0,len(word_list))
    secret_word = word_list[rand_position].upper()
    return secret_word

def init_right_letters(secret_word):
    return ["__" for letter in secret_word]

def player_input():
    guess = input("Choose a letter: ").upper().strip()
    return guess

def mark_correct_guess(secret_word,guess,right_letters):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = guess
        index += 1

def draw_hang(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def win_message():
    print("WELL DONE! Your neck is safe for now!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def loser_message(secret_word):
    print("OHH CRAP! You just got hanged...")
    print("The right word is {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == '__main__'):
    play()
