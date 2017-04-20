# Exercicio referente ao problema numero 1045 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
# Por: Renan Santana Desiderio

n = raw_input().split()
n.sort()
n.reverse()
a = float(n[0])
b = float(n[1])
c = float(n[2])

if a>=(b+c):
	print "NAO FORMA TRIANGULO"
elif (a*a)==(b*b)+(c*c):
	print "TRIANGULO RETANGULO"
elif (a*a)>(b*b)+(c*c):
	print "TRIANGULO OBTUSANGULO"
elif (a*a)<(b*b)+(c*c):
	print "TRIANGULO ACUTANGULO"

if (a==b==c):
	print "TRIANGULO EQUILATERO"
elif a<(b+c) and (b==c):
	print "TRIANGULO ISOSCELES"