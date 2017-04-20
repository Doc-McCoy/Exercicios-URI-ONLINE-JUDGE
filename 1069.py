# Exercicio referente ao problema numero 1069 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1069
# Por: Renan Santana Desiderio

m = 0
q = 0
for i in range(10):
	n = input()
	q+=1
	if n>m:
		m=n
		q=q
print m
print q