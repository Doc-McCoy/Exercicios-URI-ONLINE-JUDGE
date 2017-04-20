# Exercicio referente ao problema numero 1030 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1030
# Por: Renan Santana Desiderio

nc=input() # casos

for i in range(nc):
	l=raw_input().split()
	n=int(l[0]) # pessoas
	k=int(l[1]) # salto

	homens=range(1,n+1) # Lista de homens numerados
	