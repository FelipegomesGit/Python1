# crie um programa que  leia uma frase pelo teclado e mostre 
#Quantas vezes a leta A aparece 
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez
frase=str(input('Digite um frase: ')).strip()
tamanho = frase.upper().count('A')
comeco=frase.upper().find('A')
print ('A letra "A" aparece {} vezes. '.format(tamanho))
print ('A letra A pararece na posição {} pela primeira vez'.format(comeco))