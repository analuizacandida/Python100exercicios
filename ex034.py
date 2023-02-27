import time
from random import randint
computador = randint(0,5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número estou pensando?'))
print('PROCESSANDO...')
time.sleep(3)
if jogador==computador:
    print('Parabéns! Você consegiu me vencer!')
else:
    print('Ganhei!! Eu pensei no número {} e não no {}!'.format(computador,jogador))
