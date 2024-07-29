# crie um programa que leia o peso de 5 pessoas e mostre qual foi o maior e o menor
pmaior=0
pmenor=0
for c in range (1, 6):
    peso = float (input("Digite o {} peso: ".format (c)))
    if peso > pmaior:
        pmaior=peso
    if peso < pmenor:
        pmenor=peso
print('O maior peso digitado foi {}.'.format(pmaior))
print('O menor peso digitado foi {}.'.format(pmenor))
