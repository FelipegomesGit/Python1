# mostre um PA usando while
print ('Gerador de PA')
primeiro = int (input('Informe o primeiro termo: '))
razao = int (input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('->',termo, end='')
        termo += razao
        cont += 1
    print('\nPAUSA')
    mais = int (input('Quantos termos você quer mostrar a mais? '))
        
    

    
