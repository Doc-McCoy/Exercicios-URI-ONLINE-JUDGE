# Exercicio referente ao problema numero 1131 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1131
# Por: Renan Santana Desiderio

placarInt=0
placarGrem=0
empate=0
grenais=1
while True:
	n=raw_input().split()
	grenInt = int(n[0])
	grenGrem = int(n[1])
	if grenInt == grenGrem:
		empate+=1
	elif grenInt > grenGrem:
		placarInt+=1
	elif grenGrem > grenInt:
		placarGrem+=1
	print "Novo grenal (1-sim 2-nao)"
	d=input()
	if d == 1:
		grenais+=1
		continue
	else:
		break

print "%i grenais" %grenais
print "Inter:%i" %placarInt
print "Gremio:%i" %placarGrem
print "Empates:%i" %empate
if placarInt>placarGrem:
	print "Inter venceu mais"
elif placarGrem>placarInt:
	print "Gremio venceu mais"