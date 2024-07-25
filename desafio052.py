#faca um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int (input('Digite um numero para saber se ele é primo: '))
p=0
d=0
for c in range (1, num +1):      
          if (num % c) == 0:
             print('\033[33m', end='')
             p += 1
          else:
             print('\033[31m', end='')  
          print('{} '.format(c), end='')  
print ('\n O numero {} foi divisivel {} vezes'.format(num, p))
if p ==2:
     print('E por isso ele é primo')
else:
     print ('E por isso não é primo')
            