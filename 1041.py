# Exercicio referente ao problema numero 1041 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
x, y = n
x = float(x)
y = float(y)

if x>0 and y>0:
	print 'Q1'
elif x>0 and y<0:
	print 'Q4'
elif x<0 and y>0:
	print 'Q2'
elif x<0 and y<0:
	print 'Q3'
elif x==0 and y==0:
	print "Origem"
elif x==0:
	print "Eixo Y"
elif y==0:
	print "Eixo X"