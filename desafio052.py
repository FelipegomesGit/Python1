#faca um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int (input('Digite um numero para saber se ele é primo: '))
p=0
d=0
for c in range (1, num):
    p = num % 3
    d = num % 5
    if p == 0 and d==0:
        print (c)