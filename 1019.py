# Exercicio referente ao problema numero 1019 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
# Por: Renan Santana Desiderio

n = input()

horas = n/3600
minutos = (n-horas*3600)/60
segundos = n-(int(horas)*3600)-(int(minutos)*60)

print "%i:%i:%i" % (horas, minutos, segundos)