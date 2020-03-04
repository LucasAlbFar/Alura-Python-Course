import hangman
import guessing_game

def menu():
    print('+++++++++++++++++++++++++++++')
    print('          Py Games!          ')
    print('+++++++++++++++++++++++++++++')
    print(' ')
    print('(1) Hangman (2) Guessing Game')
    game  = int(input('What game do you choose? '))

    while (game < 1 or game > 2):
        game = int(input('I can find this game....could you try a valid option? '))

    if (game == 1):
        hangman.play()

    elif (game == 2):
        guessing_game.play()

if (__name__ == '__main__'):
    menu()