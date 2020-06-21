import adivinhacao
import forca
from time import sleep
print('~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~Central de jogos~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~')
sleep(1)
print('''[1] Adivinhação 
[2] Forca''')
op = int(input("Qual jogo deseja jogar:"))
if op == 1:
    print('Abrindo Jogo da Advinhação', end='')
    for p in range(1,4):
        print('.', end='')
        sleep(1)
    print()
    adivinhacao.jogar_adivinhacao()
if op == 2:
    print('Abrindo Jogo da Forca', end='')
    for p in range(1, 4):
        print('.', end='')
        sleep(1)
    print()
    forca.jogar_forca()



