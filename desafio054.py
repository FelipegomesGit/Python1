# Crie um programa que leia o ano de nascimento de 7 pessoas e diga quantas são maiores de idade e quantas não são...
import datetime
for c in range (0, 7):
    nas = int (input('Digite seu ano de nascimento utilizando o formato xxxx (ex: 2024): '))
    if 1900 <= nas <= 2024:
        print (" seu ano foi aceito")
        
    else:
        print ('ano não aceito')
    