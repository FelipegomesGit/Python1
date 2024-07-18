# escreva um programa que leia a velocidade de um carro e se ele ultrapassar 80km informe que ele será multado.
# a multa vai custar 7 reais por cada km acima
km=int(input('Digite a velocidade: '))
if km > 80:
    print('Você será multado')
    multa = (km - 80) * 7
    print ('Sua multa sé de {:.2f} reais.'. format (multa))
else:
    print("Parabéns você esta no limite correto de velocidade")
