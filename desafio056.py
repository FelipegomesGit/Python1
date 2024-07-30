# um programa que peça nome, idade e sexo de 4 pessoas
#mosntre a media das idades, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
for c in range (0, 4):
    nome = str (input("Digite o nome da {} pessoa: ".format(c))).strip()
    idade = int (input("Digite a idade da {} pessoa: ".format(c)))
    sexo = int (input('Informe o seu genero e F: [M, F]'))
