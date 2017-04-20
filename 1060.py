# Exercicio referente ao problema numero 1060 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060
# Por: Renan Santana Desiderio

i = 0
pos = 0
while i <=5:
	n = input()
	if n>0:
		pos+=1
	i+=1
print "%i valores positivos" % pos