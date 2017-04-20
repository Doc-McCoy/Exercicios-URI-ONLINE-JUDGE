# Exercicio referente ao problema numero 1012 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012
# Por: Renan Santana Desiderio

entrada = raw_input()
entrada = entrada.split(" ")
a, b, c = entrada

triangulo = (float(a)*float(c))/2
circulo = 3.14159*(float(c)*float(c))
trapezio = (float(a)+float(b))*float(c)/2
quadrado = float(b)*float(b)
retangulo = float(a)*float(b)

print "TRIANGULO: %.3f" %triangulo
print "CIRCULO: %.3f" %circulo
print "TRAPEZIO: %.3f" %trapezio
print "QUADRADO: %.3f" %quadrado
print "RETANGULO: %.3f" %retangulo