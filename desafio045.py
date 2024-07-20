#Jpkenpo (pedra, papel e tesolra)
import random
mao=str(input('Ecolha entre PEDRA, PAPEL E TESOURA: ')).strip().upper()
comp= random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
if 'PAPEL'>'TESOURA':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'PAPEL'>'PEDRA':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'TESOURA'>'PAPEL':
    print ('{} MAIOR DO QUE {} '.format(mao, comp))
elif 'PAPEL'=='PAPEL' and 'PEDRA'=='PEDRA' and 'TESOURA' =='TESOURA':
    print (mao, comp)



    