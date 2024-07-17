# faça um programa que leia o nome completo da pessoa, mostrando em seguida o primeiro e ultimo nome.
nome=str(input('Digite seu nome completo: ')).strip()
nomediv=nome.split()
fim=nome.rsplit()
print('Seu primeiro nome é {} '.format(nomediv[0]))
print('Seu primeiro nome é {} '.format(fim[-1]))
