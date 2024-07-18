# peça para digitar um numero de 0 até 5 e o usuário tenta descobrir qual numero o computador escolheu
from random import randint
num = randint (0, 5) # escolhe numero de 0 até 5
jogador=int(input('Digite um numero entre 0 a 5: '))
if jogador == num:     
    print ('Parabéns você acertou o  numero {}'. format (num))
else:
print ('Você errou o numero')