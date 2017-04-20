# Exercicio referente ao problema numero 1101 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1101
# Por: Renan Santana Desiderio

while True:
	line=raw_input().splite()
	lis = [int(line[0]), int(line[1])]
	lis.sort()
	m = lis[0]
	n = lis[1]
	print range(m,n+1)