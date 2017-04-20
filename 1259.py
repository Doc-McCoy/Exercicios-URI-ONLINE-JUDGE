# Exercicio referente ao problema numero 1259 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1259
# Por: Renan Santana Desiderio

n=input()
par=[]
impar=[]

for i in range(n):
	i=input()
	if i%2==0:
		par.append(i)
	else:
		impar.append(i)

par.sort()
impar.sort()
impar.reverse()

for i in par:
	print i
for i in impar:
	print i