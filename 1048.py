# Exercicio referente ao problema numero 1048 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048
# Por: Renan Santana Desiderio

sal = input()

if sal <= 400.00:
	novosal = sal*1.15
	print "Novo salario: %.2f" % novosal
	print "Reajuste ganho: %.2f" % (novosal-sal)
	print "Em percentual: 15 %"

elif sal <= 800.00:
	novosal = sal*1.12
	print "Novo salario: %.2f" % novosal
	print "Reajuste ganho: %.2f" % (novosal-sal)
	print "Em percentual: 12 %"

elif sal <= 1200.00:
	novosal = sal*1.1
	print "Novo salario: %.2f" % novosal
	print "Reajuste ganho: %.2f" % (novosal-sal)
	print "Em percentual: 10 %"

elif sal <= 2000.00:
	novosal = sal*1.07
	print "Novo salario: %.2f" % novosal
	print "Reajuste ganho: %.2f" % (novosal-sal)
	print "Em percentual: 7 %"

elif sal > 2000.00:
	novosal = sal*1.04
	print "Novo salario: %.2f" % novosal
	print "Reajuste ganho: %.2f" % (novosal-sal)
	print "Em percentual: 4 %"