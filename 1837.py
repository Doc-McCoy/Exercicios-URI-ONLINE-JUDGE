# Exercicio referente ao problema numero 1837 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1837
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
a = int(n[0])
b = int(n[1])
q = a/b
r = a%b

print '%i %i' % (q,r)