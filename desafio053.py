# palindromo (frases de tras para frente)
import re
frase = str (input ('Digite uma frase para eu confirmar se é um palindromo: ')).strip()
texto = re.sub(r"[^\w\s]", "", frase.lower()) #utilizamos a biblioteca re para remover todos os caracteres que não são letras ou espaços. Em seguida, convertemos a string para letras minúsculas e realizamos a comparação.
if frase == texto[::-1]: # faz o inverso da frase
        print ('Essa frase é um palindromo')
else:
        print ('Não é um palindromo')
          
    
        

