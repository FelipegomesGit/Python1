# um programa que peça nome, idade e sexo de 4 pessoas
#mosntre a media das idades, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
soma=0
media=0
for c in range (1, 5):
    nome = str (input("Digite o nome da {} pessoa: ".format(c))).strip()
    idade = int (input("Digite a idade da {} pessoa: ".format(c)))
    sexo = str (input('Informe o seu genero [M/F]: ')).upper()[0]
    soma = soma + idade #faz a soma entre todas as idades
    media = soma / c #pegaa soma das idades e divide pelo numero de pessoas
    print(media)
    print(soma)


