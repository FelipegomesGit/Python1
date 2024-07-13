# Leia um angulo qualquer e mostre o seu valor em Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
rad  = float (input ('Digite o valor do angulo: ')) 
s=sin(radians(rad))
c=cos(radians(rad))
t=tan(radians(rad))
print (' O seu valor em seno: {:.2f} \n Em cosseno: {:.2f} \n E Tangente: {:.2f}'.format (s, c, t ))
