# Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
c = input('Digite o nome da cidade: ').strip().split() #remove os espaços
print(c[0].upper() == 'SANTO')

'''
Solução do vídeo

palavra=str(input('Digite o nome da cidade: ')).strip()
print('Essa cidade é {} para palavra "Santo" '.format (palavra[:5].upper() =='SANTO'))'''
