# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome=str(input('Digite seu nome completo: ')).strip()
n = nome.upper().split()
print('SILVA' in n)