# Exercicio referente ao problema numero 1038 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
cod, quant = n

tabela = {
	1 : 4.0, 
	2 : 4.5,
	3 : 5.0,
	4 : 2.0,
	5 : 1.5}

print "Total: R$ %.2f" % (tabela[int(cod)] * int(quant))