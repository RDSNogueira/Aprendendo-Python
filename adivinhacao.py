from random import randint
from time import sleep
def jogar_adivinhacao():
    print('                     ----------------------------------------')
    print('                               Jogo da Adivinhação')
    print('                     ----------------------------------------')
    print('====================================================================================')
    print('Adivinhe o número que o computador escolheu no menor número de tentativas possíveis.')
    print('====================================================================================')
    print('''[1] Fácil (20 tentativas
[2] Médio (10 tentativas
[3] Difícil (5 tentativas)''')
    numero = randint(1, 101)
    cont = 1
    pontos = 1000
    nivel = int(input('Escolha um nível:'))

    while nivel not in range(1, 4):
        nivel = int(input('Por favor, escolha um nível de 1 a 3:'))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    for timer in range(1, 4):
        print(timer, end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
    print('Já!')
    sleep(1)
    while cont <= tentativas:
        print(f'Tentativa {cont} de {tentativas}.')
        chute = int(input('Escolha um número de 1 a 100:'))
        if chute not in range(1, 101):
            print('Somente números de 1 a 100...Tente novamente: ')
            print('---------------------------------------------')
            continue
        acerto = chute == numero
        maior = chute > numero
        menor = chute < numero
        if acerto:
            print('*'*13)
            print('Você acertou!')
            print('*'*13)
            break
        else:
            if maior:
                    print('-' * 48)
                    print('Seu número é MAIOR do que o escolhido pelo computador.')
                    print('-' * 48)
            if menor:
                    print('-' * 48)
                    print('Seu número é MENOR do que o escolhido pelo computador.')
                    print('-' * 48)
            pontos_perdidos = abs(chute - numero)
            pontos = pontos - pontos_perdidos
        cont += 1
    if acerto:
        print(f'Você acertou o número {numero} em {cont} tentativas!')
        print(f'Sua pontuação é {pontos}')
    else:
        print('Você não conseguiu acertar! :(... Tente um nível mais fácil.')
        print(f'O número era {numero}.')
    print('Fim de jogo!')



