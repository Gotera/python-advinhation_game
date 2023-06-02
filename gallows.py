import random

def game_message():
    print('*******************')
    print('** Jogo da Forca **')
    print('*******************')

def winner_msg():
    print("Parabéns, você ganhou!")
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

def loser_msg(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
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

def draw_gallow(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def create_secret_word():
    words = []
    with open ('list.txt', encoding='utf-8', mode='r') as archive:
        for line in archive:
            line = line.strip()
            words.append(line)
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def request_guess():
    guess = input('Qual a letra?: ')
    guess = guess.strip().upper()
    return guess

def filter_kick(guess, known_letters, secret_word):
    index = 0
    for letter in secret_word:
        if(guess == letter):
            known_letters[index] = letter
        index = index + 1

def play():
    game_message()
    secret_word = create_secret_word() 
    known_letters = ["_" for letter in secret_word]
    
    hanged = False #Enforcado
    hit = False #Acertou
    errors = 0
    
    print(known_letters)
    while(not hanged and not hit):
        kick = request_guess()
        if(kick in secret_word):
           filter_kick(kick, known_letters, secret_word)
        else:
            errors += 1
            draw_gallow(errors)

        hit = "_" not in known_letters
        hanged = errors == 7

        if(hit):
            winner_msg()
            break
        
        if(hanged):
            loser_msg(secret_word)
            break
        print(known_letters)

if(__name__ == "__main__"):
    play()
    