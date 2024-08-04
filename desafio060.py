# calculo do fatorial de um numero
numero = int(input("Digite um número inteiro: "))
fatorial = 1
contador = 1
while contador <= numero:
    fatorial *= contador
    contador += 1


print("O fatorial de", numero, "é:", fatorial)

