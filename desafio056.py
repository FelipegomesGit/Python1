# um programa que peça nome, idade e sexo de 4 pessoas
#mosntre a media das idades, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
soma=0
media=0
nomevelho = ''
totalmulher = 0
for c in range (1, 5):
    nome = str (input("Digite o nome da {} pessoa: ".format(c))).strip()
    idade = int (input("Digite a idade da {} pessoa: ".format(c)))
    sexo = str (input('Informe o seu genero [M/F]: '))
    soma += idade #faz a soma entre todas as idades
    
    if c == 1 and sexo in 'Mm': # usa in para M e m por isso o in se nao poderia usar o ===
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
            if sexo in 'Ff' and idade < 20:
                totalmulher += 1
media = soma / c #pegaa soma das idades e divide pelo numero de pessoas
print('A media de idade do grupo é {}'.format (media))
print ('O home mais velho tem {} anos e se chama {} '.format (maioridadehomem, nomevelho))
print(' A somda de mulheres abaixo de 20 anos é {} .'.format(totalmulher))


