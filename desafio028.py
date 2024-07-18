# peça para digitar um numero de 0 até 5 e o usuário tenta descobrir qual numero o computador escolheu
from random import randint
num = randint(0, 5) # escolhe numero de 0 até 5
jogador=int(input('Digite um numero entre 0 a 5: '))
if jogador == (num):   
    print ('Parabéns você acertou o  numero {}'.format(jogador))
else:
    print ("Errouuuuu!!!!")
'''
import random
nums = [0, 1, 2, 3, 4, 5]
np = random.choice(nums)
print('Vou pensar em um número de 0 a 5... Tente adivinhar qual é o número!')

adivinhe = int(input('Qual é o número? '))
if adivinhe == (np):
    print('VOCÊ ACERTOU, PARABÉNS!')
else:
    print('O Computador VENCEU!')'''