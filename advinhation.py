import random

def play():
    print('*******************')
    print('Jogo de advinhação')
    print('*******************')

    secret_number = random.randrange(1,101)
    total_rounds = 0
    round = 1
    points = 1000

    print('Escolha o nível de dificuldade:')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Qual dificuldade você escolhe?: '))

    if (nivel == 1):
        total_rounds = 20
    elif(nivel == 2):
        total_rounds = 10
    else:
        total_rounds = 5

    for round in range (1, total_rounds + 1) :
        print("Tentativa {} de {}".format(round, total_rounds))
        kick_str = input('Digite o seu número: ')

        print('Você digitou', kick_str)

        kick = int(kick_str)
        hit = secret_number == kick
        highest = secret_number < kick
        smaller = secret_number > kick

        if (kick < 1 | kick > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        if (hit):
            print("Você acertou! Com um total de {} pontos".format(points))
            break
        else:
            if(highest):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(smaller):
                print("Você errou! O seu chute foi menor que o número secreto")
            missed_points = abs(secret_number - kick)
            points = points - missed_points
            
    print("Final do Jogo")

if(__name__ == "__main__"):
    play()
    