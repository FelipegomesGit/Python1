# Crie um programa que leia um numero de 0 ate 9999 e mostre na telacada um dos digitos separados.
num=int(input ('digite um numero entre 0 e 9999: '))
n=str(num)
print ('Analisando o numero{}'.format(num))
print ('Unidade: {}'.format(n[3]))
print ('Dezena: {}'.format(n[2]))
print ('Centena: {}'.format(n[1]))
print ('Milhar: {}'.format(n[0]))