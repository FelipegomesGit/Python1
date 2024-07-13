# Teorema de pitagoras
from math import sqrt
catop = float( input ('Digite o valor do Cateto oposto: '))
catad = float( input ('Digite o valor do Cateto adjacente: '))
hipo = sqrt((catop * catop) + (catad*catad))
print ('A medida da Hipotenusa é: {}'.format (hipo))

