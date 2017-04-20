# Exercicio referente ao problema numero 1132 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1132
# Por: Renan Santana Desiderio

x=input()
y=input()
total=int()
organizer=[x,y]
organizer.sort()
x=organizer[0]
y=organizer[1]

for i in range(x,y+1):
	if i%13!=0:
		total+=i
print total