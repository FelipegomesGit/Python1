# faca um programa que leia 4 alunos e mostre a ordem de apresentação deles
import random
nome1= str(input ('Digite o nome do primeiro aluno: '))
nome2= str(input ('Digite o nome do segundo aluno: '))
nome3= str(input ('Digite o nome do terceiro aluno: '))
nome4= str(input ('Digite o nome do quarto aluno: '))
escolhido = [nome1, nome2, nome3, nome4]
random.shuffle(escolhido)
print ('A ordem foi: {}'.format (escolhido))
