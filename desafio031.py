km=float(input('Digite a distância da sua viagem: '))
if km <200:
    km1=km*0.50
    print ('O valor da sua passagem será de {:.2f} reais por ser menor de 200km'.format(km1))
else:
    km2= km*0.45
    print ('O valor da sua passagem será de {:.2f} reais por ser maior de 200km'.format(km2))

#ou preco = distancia *0.50 if km <200 else distancia *0.45 