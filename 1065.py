# Exercicio referente ao problema numero 1065 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1065
# Por: Renan Santana Desiderio

q=0
for i in range(5):
	n = input()
	if n % 2 == 0:
		q += 1
print "%i valores pares" % q
