# Exercicio referente ao problema numero 1010 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010
# Por: Renan Santana Desiderio

lista1 = raw_input() # Armazena os numeros como STRING
lista2 = raw_input() # Armazena os numeros como STRING

lista1 = lista1.split(" ") # Divide a lista1 nos espacos em branco
lista2 = lista2.split(" ") # Divide a lista2 nos espacos em branco

cod1, quant1, valor1 = lista1 # Atribui cada string dividida em uma variavel
cod2, quant2, valor2 = lista2 # Atribui cada string dividida em uma variavel

TOTAL = int(quant1)*float(valor1)+int(quant2)*float(valor2)

print "VALOR A PAGAR: R$ %.2f" % TOTAL