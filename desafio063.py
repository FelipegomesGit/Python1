# sequencia de fibonacci
num = int (input ('Informe os numero de elementos da sequencia de fibonacci que deseja: '))
f = 0
f2 = 1
f3 = 1
c = 3
print(f)
print(f2)
while c <= num:
    f3 = f + f2
    print (f3)
    f=f2
    f2=f3
    c += 1
print ('FIM')