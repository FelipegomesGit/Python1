#Jpkenpo (pedra, papel e tesolra)

from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-="*20)
print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[perguntar]))
print("-="*20)

if computador == 0: # computador jogou pedra
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1: #computador jogou papel
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2: # tesoura
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")


'''import random
mao=str(input('Ecolha entre PEDRA, PAPEL E TESOURA: ')).strip().upper()
comp= ('PEDRA', 'PAPEL', 'TESOURA')
computa= randint(0,2)
if 'PEDRA'>'TESOURA':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'PAPEL'>'PEDRA':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'TESOURA'>'PAPEL':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'PAPEL'=='PAPEL' and 'PEDRA'=='PEDRA' and 'TESOURA' =='TESOURA':
    print (mao, comp)'''



    