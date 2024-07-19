# leia 3 numeros e mostre qual o maior e qual o menor
a=int(input('Informe o primeiro numero: '))
b=int(input('Informe o segundo numero: '))
c=int(input('Informe o terceiro numero: '))
#verifica quem é menor 
menor=b
if b < a and b<c:
    menor = a
if c < a and c<b:
    menor = c
#verificando Maior
if b > a and b > c:
    maior = b
if c> a and c>b:
    maior= c
print ( 'MAior é {}'.format (maior))
print ( 'Menor é {}'.format (menor))

   

