# crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar , 2 multiplicar , 3 maior , 4 novos numeros e 5 sair do programa
num1 = int (input ('Digite o primeiro numero inteiro: ' ))
num2 = int (input ('Digite o segundo numero inteiro: ' ))
menu = ''
soma = 0
mult = 0
while True:
    print ('='*50)
    print ('Escolha de acordo com o menu abaixo: \n')
    print (' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa \n')
    menu = int (input('Digite a opção escolhida: '))
    if menu == 5:
        break
    if menu == 1:
        soma = num1 + num2
        print ('O resultado da soma é {} '.format(soma))
    if menu == 2:
        mult = num1 * num2
        print(' O resultado da multiplicação é {}'. format(mult))
    if menu == 3:
        if num1 > num2:
            print('O numero {} (Primeiro digitado) é maior que o {} (segundo digitado).'. format (num1, num2))
        elif num2 > num1:
            print('O numero {} (segundo digitado) é maior que o {} (primeiro digitado).'. format (num2, num1))
        else:
            print('Eles são iguais')
    if menu == 4:
        num1 = int (input ('Digite outro primeiro numero inteiro: ' ))
        num2 = int (input ('Digite outro segundo numero inteiro: ' ))



            
        


        

        