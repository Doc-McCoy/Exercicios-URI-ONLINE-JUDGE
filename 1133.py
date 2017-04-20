# Exercicio referente ao problema numero 1133 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1133
# Por: Renan Santana Desiderio

x=input()
y=input()
org=[x,y]
org.sort()
x=org[0]
y=org[1]
valores=list()

for i in range(x+1,y):
	if i%5==2 or i%5==3:
		valores.append(i)
valores.sort()
for i in valores:
	print i