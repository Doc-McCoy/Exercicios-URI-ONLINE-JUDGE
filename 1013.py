# Exercicio referente ao problema numero 1013 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013
# Por: Renan Santana Desiderio

lista = raw_input()
lista = lista.split(" ")

a, b, c = lista
a = int(a)
b = int(b)
c = int(c)

maiorab = (a+b+abs(a-b))/2
maiorxc = (maiorab+c+abs(maiorab-c))/2

print "%i eh o maior" % maiorxc