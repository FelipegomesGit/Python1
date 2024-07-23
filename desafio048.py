#faça um programa que faça que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram em um intervalo entre 1 até 500
print('multiplos de 3')
s=0
cont=0
for c in range (1, 501, 2):
    if (c%3) == 0:
        s += c
        cont += 1
print (s)
print('A Soma de todos os valores impares divisiveis por 3 é {}'.format(cont))