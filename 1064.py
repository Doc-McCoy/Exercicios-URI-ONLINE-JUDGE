# Exercicio referente ao problema numero 1064 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064
# Por: Renan Santana Desiderio

pos = 0
soma = 0
for i in range(6):
	num = input()
	if num >=0:
		pos += 1
		soma += num

print "%i valores positivos" % pos
print "%.1f" % (soma/pos)
