# desenvolva um programa que leia seis numeros inteiros e mostre apenas a soma daqueles que forem pares. Se o valor da digitação for impar desconsidere
s=0
for c in range (0, 6):
   num = int(input('Digite um numero: '))
   if num % 2 == 0:
      s += num
print ('A soma dos numeros pares é {} '. format(s))
      