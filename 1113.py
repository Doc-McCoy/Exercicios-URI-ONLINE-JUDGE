# Exercicio referente ao problema numero 1113 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1113
# Por: Renan Santana Desiderio

n = raw_input().split()
x=int(n[0])
y=int(n[1])

while x!=y:

	if x<y:
		print "Crescente"
	elif x>y:
		print "Decrescente"

	n = raw_input().split()
	x=int(n[0])
	y=int(n[1])