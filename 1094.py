# Exercicio referente ao problema numero 1094 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1094
# Por: Renan Santana Desiderio

t=input()
cob=0
coe=0
rat=0
sap=0

for i in range(t):
	n=raw_input().split()
	quant=int(n[0])
	tipo=n[1]

	cob+=quant
	if tipo=='C':
		coe+=quant
	elif tipo=='R':
		rat+=quant
	elif tipo=='S':
		sap+=quant

print "Total: %i cobaias"    % cob
print "Total de coelhos: %i" % coe
print "Total de ratos: %i"   % rat
print "Total de sapos: %i"   % sap
print "Percentual de coelhos: %.2f %%" % (100*coe/float(cob))
print "Percentual de ratos: %.2f %%"   % (100*rat/float(cob))
print "Percentual de sapos: %.2f %%"   % (100*sap/float(cob))