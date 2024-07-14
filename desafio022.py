# Crie um programa que mostre
# O nome com todas a letras Maiusculas
#O nome com todas minusculas
#quantas letras tem sem considerar os espaços
#quantas letras tem o primeiro nome

nome =str(input('Digite seu nome completo: ')).strip()# strip para eliminar os espaços do inicio e fim que podem ser digitados e evita o erro de conta
print(nome)

print('======================================================================')
print('Seu nome em maiusculas é {}'.format (nome.upper()))
print('Seu nome em minusculas é {}'.format (nome.lower()))
dividido=len(nome) - nome.count(" ") # Conta o nome menos os espaços
print('A quantidade de caracteres de {} sem espaços é {}'. format (nome,dividido))
print('Seu primeiro nome tem {} letras.'.format (nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'. format(separa[0], len(separa[0])))# split conta o primeiro nome com o uso do [0] e o len separa todos e exibe o nome identificado como [0]

