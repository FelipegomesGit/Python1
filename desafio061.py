# mostre um PA usando while
print ('Gerador de PA')
primeiro = int (input('Informe o primeiro termo: '))
razao = int (input('Razão da PA: '))
termo = primeiro
cont = 1
add = 0
while cont <= 10:
    print('->',termo, end='')
    termo +=razao
    cont += 1
    add = int (input('Quantos termos você quer mostrar a mais? '))
    while add != 0:
        print(add)
    

    
