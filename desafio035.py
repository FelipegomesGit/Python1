# informe 3 numeros para saber se eles formam um triangulo
a=int(input('Informe a primeira reta: '))
b=int(input('Informe a segunda reta: '))
c=int(input('Informe a terceira reta: '))
if a < b+c and b<a+c and c<a+b:
    print ('Eles formam um triangulo!')
else:
    print (' Não formam um triangulo!')