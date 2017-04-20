# Exercicio referente ao problema numero 1115 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1115
# Por: Renan Santana Desiderio

n=raw_input().split()
x=int(n[0])
y=int(n[1])

while x!=0 or y!=0:
	
	if x>0 and y>0:
		print "primeiro"
	elif x<0 and y>0:
		print "segundo"
	elif x<0 and y<0:
		print "terceiro"
	elif x>0 and y<0:
		print "quarto"

	n=raw_input().split()
	x=int(n[0])
	y=int(n[1])