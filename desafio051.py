#desolva um programa que leia o primeiro termo e a razao de uma PA. no final mostre os primeiros termos dessa razão
''' i = int (input('Inicio: '))
f = int (input('Fim: '))
p = int (input('Passo: '))
for c in range (i, f+1, p):
    print (c)
print ('FIM')'''

n1 = int(input('Digite o primeiro termo da P.A. : '))

razao = int(input('Digite a razão da P.A. : '))

decimo = n1 + (10 - 1) * razao #10 - 1 pois vc quer achar o decimo termo, essa é a formula matematica

for c in range(n1,decimo + razao, razao):
    formula = n1 + razao

    print(c, end=' --> ')
print('FIM')