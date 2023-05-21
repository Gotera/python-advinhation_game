print('Jogo de advinhação')

secret_number = 42
kick_str = input('Digite o seu número: ')

print('Você digitou', kick_str)

kick = int(kick_str)

if (secret_number == kick):
    print("Você acertou!")
else:
    print("Você errou!")
