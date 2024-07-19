# escreva um programa que aponte a compra de um casa ele vai perguntar o valor da casa, seu salario e em quanto anos ele quer pagar.
# calcule o valor da prestação 


valorcasa = float(input("Qual o valor da casa? "))
valorwage = float(input("Qual o seu salário? "))
anospay = int(input("Em quantos anos pretende pagar? "))

parcela = valorcasa/(anospay*12)

if parcela>(30/100)*valorwage:
    print ("Você é liso, seu empréstimo foi negado")
else:
    print (("Nós vamos te emprestar e a parcela será de R${:.2f}").format (parcela))

