import random

print('*******************')
print('Jogo de advinhação')
print('*******************')

total_rounds = random.randrange(1,101)
round = 1

for round in range (1, total_rounds + 1) :
    secret_number = 42
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
        print("Você acertou!")
        break
    else:
        if(highest):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(smaller):
            print("Você errou! O seu chute foi menor que o número secreto")

    print("Final do Jogo")