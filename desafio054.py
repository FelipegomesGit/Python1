# Crie um programa que leia o ano de nascimento de 7 pessoas e diga quantas são maiores de idade e quantas não são...
import datetime
cont=0
contm = 0
for c in range (1, 8):
    nas = int (input('Digite o ano de nascimento da {} utilizando o formato xxxx (ex: 2024): '.format(c)))
    if 1900 <= nas <= 2024:
        print (" seu ano foi aceito")
        if 2006 >= nas:
            cont += 1
            print ('Você já pode dirigir!')
        else:
            print ("Você ainda é um bebe!")
            contm += 1
               
    else:
        print ("seu ano não foi aceito! favor corrigir!")
print (' temos um total de {} maior de idade e {} menor de idade.'. format (cont, contm))
    