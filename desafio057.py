# faça um programa que leia o sexo de uma pessoa,  mas só aceite os valores de 'M' ou "F". caso esteja errado peça digitação novamente.
sexo = ' '
sexo = str (input ('Digite corretamente seu sexo: [F/M]: ')).upper()
while sexo != 'F' and sexo !='M':
    sexo = str (input ('Digite Novamente seu sexo: [F/M]: ')).upper()
    
print ('Caractere Aceito!')

                
                