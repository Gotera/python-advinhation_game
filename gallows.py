def play():
    print('*******************')
    print('** Jogo da Forca **')
    print('*******************')

    secret_word = 'banana'
    hanged = False
    hit = False

    while(not hanged and not hit):
        print('Jogando...')

        kick = input('Qual a letra?: ')
        index = 0
        for letter in secret_word:
            if(kick == letter):
                print("Você acertou a letra {} na posição {}".format(letter, index))
            index = index + 1

    print('Fim de Jogo')

if(__name__ == "_main_"):
  play()
