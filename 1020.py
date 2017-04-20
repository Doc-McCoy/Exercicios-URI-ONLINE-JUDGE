# Exercicio referente ao problema numero 1020 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
# Por: Renan Santana Desiderio

idade = input()

anos = idade/365
idade -= int(anos)*365
meses = idade/30
idade -= int(meses)*30
dias = int(idade)

print "%i ano(s)"  %anos
print "%i mes(es)" %meses
print "%i dia(s)"  %dias