#faca um programa que mostre uma conyagem regressiva de 10 até 0 com uma pausa de 1 segundo
import time
print('Vai começar a contagem...')
for c in range (10, 0, -1):
    time.sleep(1)
    print(c)
print ('ACABOUUUUU!!!')