# Exercicio referente ao problema numero 1044 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
a = int(n[0])
b = int(n[1])

if a%b == 0 or b%a == 0:
	print "Sao Multiplos"
else:
	print "Nao sao Multiplos"