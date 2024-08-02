# desafio 028 onde o computador vai pensar em um numero de 0 e10. jogador vai advinhar até acertar o numero do computador. Final comptabilizar o numero de tentativas.

from random import randint
cont = 0
num = randint(0, 10) # escolhe numero de 0 até 10
jogador=int(input('Digite um numero entre 0 a 10 e tente adivinhar o que estou pensando...: '))
while jogador != (num):
    print ("Errouuuuu!!!!")
    jogador=int (input(('Tente novamente...: ')))   
    cont += 1
    
print ('Parabéns você acertou!! Precisou de {} vezes para acertar'.format(cont))