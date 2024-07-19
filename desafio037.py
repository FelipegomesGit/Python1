# escreva um programa que leia um numero inteiro e peça ao usurio para escolher qual base de conversão
num=int(input('Digite o valor a ser convertido: '))
conversao=int(input(" Digite o valor entre 1 - Decimal, 2 - Octal e 3 - Hexadecimal: "))
if conversao == 1:
    print ("Seu numero em binário é {}".format((bin(num))))
elif conversao == 2:
    print ('Seu numero em Octa é igual a {}'.format((oct(num))))
else:
    conversao==3
    print('Seu valor em hexadecimal é {}'.format((hex(num))))