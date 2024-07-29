# Crie um programa que leia o ano de nascimento de 7 pessoas e diga quantas são maiores de idade e quantas não são...
import datetime
cont=0
contm = 0
for c in range (0, 7):
    nas = int (input('Digite seu ano de nascimento utilizando o formato xxxx (ex: 2024): '))
    if 1900 <= nas <= 2024:
        print (" seu ano foi aceito")
        if 2008 >= nas:
            cont += 1
            print ('Você já pode dirigir!')
        else:
            print ("Você ainda é um bebe!")
            contm += 1
               
    else:
        print ("seu ano não foi aceito! favor corrigir!")
print (' temos um total de {} maior de idade e {} menor de idade.'. format (cont, contm))
    