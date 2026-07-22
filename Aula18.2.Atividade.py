# import math

# numero = float(input("\nDigite o seu número: "))
# raiz = math.sqrt(numero)
# print ("\nA raiz quadrada é: ",raiz)

# from math import sqrt

# numero = float(input("\nDigite o seu número: "))
# raiz = sqrt(numero)
# print ("\nA raiz quadrada é: ",raiz)

# print (math.pow)
# print (math.ceil)
# print (math.floor)
# print (math.fabs)
# print (math.sin)
# print (math.cos)
# print (math.tan)
# print (math.radians)
# print (math.)
# print (math.)
# print (math.)
# print (math.)
# print (math.)
# print (math.)

from math import radians, sin, cos, tan

angulo = float(input("\nDigite o ângulo: "))

seno = sin(radians(angulo))
print ("\nO ângulo de {} tem o seno de {:.1}".format(angulo,seno))

cosseno = cos(radians(angulo))
print ("\nO ângulo de {} tem o cosseno de {:.1}".format(angulo, cosseno))

tangente = tan(radians(angulo))
print ("\nO ângulo de {} tem a tangente de {:.1}".format(angulo, tangente))
