# crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar , 2 multiplicar , 3 maior , 4 novos numeros e 5 sair do programa
menu = ''
while menu != 5:
    num1 = int (input ('Digite o primeiro numero inteiro: ' ))
    num2 = int (input ('Digite o segundo numero inteiro: ' ))
    print ('Agorra escolha de acordo com o menu abaixo: \n')
    menu = int (input (' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa \n'))
    if menu != 1:
        soma = num1 + num2
        print ('O resultado da soma é {} '.soma)