# Exercicio referente ao problema numero 1009 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
# Por: Renan Santana Desiderio

nome = raw_input()
fixo = input()
vendas = input()
comissao = vendas*0.15

print "TOTAL = R$ %.2f" % (fixo+comissao)