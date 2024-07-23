# tabuada de um numero que usuário digitou
num = int (input ('Digite um valor que retornarei com a sua tabuada: '))
for c in range (0, 11):
    r = num*c
    print(' {} x {} = {}'. format(num, c, r) )
print ('FIM')