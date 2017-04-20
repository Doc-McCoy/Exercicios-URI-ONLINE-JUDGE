# Exercicio referente ao problema numero 1018 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
# Por: Renan Santana Desiderio

valor = input()
print valor

nota1 = 0
nota2 = 0
nota5 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0

while (valor-100) >= 0:
	nota100 += 1
	valor -= 100

while (valor-50) >= 0:
	nota50 += 1
	valor -= 50

while (valor-10) >= 0:
	nota10 += 1
	valor -= 10

while (valor-5) >= 0:
	nota5 += 1
	valor -= 5

while (valor-2) >= 0:
	nota2 += 1
	valor -= 2

while (valor-1) >= 0:
	nota1 += 1
	valor -= 1

print "%i nota(s) de R$ 100,00" %nota100
print "%i nota(s) de R$ 50,00"  %nota50
print "%i nota(s) de R$ 20,00"  %nota20
print "%i nota(s) de R$ 10,00"  %nota10
print "%i nota(s) de R$ 5,00"   %nota5
print "%i nota(s) de R$ 2,00"   %nota2
print "%i nota(s) de R$ 1,00"   %nota1