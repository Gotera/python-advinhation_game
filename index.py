import advinhation
import gallows

def choose_game():
    print('*******************')
    print('* Escolha seu Jogo *')
    print('*******************')

    print('(1) Advinhação (2) Forca')
    game = int(input('Escolha seu Jogo: '))

    if (game == 1):
        print('Jogando Forca')
        advinhation.play();
    elif (game == 2):
        print('Jogando Advinhação')
        gallows.play();

if(__name__ == "__main__"):
    choose_game()
    