# Exercicio referente ao problema numero 1042 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
n1, n2, n3 = n
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
ordem = [n1,n2,n3]
ordem.sort()
print ordem[0]
print ordem[1]
print ordem[2]
print ""
print n1
print n2
print n3