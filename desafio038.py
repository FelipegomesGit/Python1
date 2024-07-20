# faca um programa que leia dois numeros e mostre qual deles é o maior (comparando)
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
if n1>n2:
    print('O {} é maior do que {}'.format (n1,n2))
elif n2>n1:
    print('O {} é maior do que {}'.format (n2,n1))
else:
    print('{} eles são iguais {}'.format(n1,n2))
    