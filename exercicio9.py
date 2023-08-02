'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

num = float(input("Informe um número: "))

pro = num + 0
elevado = math.pow(num,2)
rai= math.sqrt(num)

print(" O valor do próprio número é", pro, "O quadrado do número informado é:", elevado, "A raíz quadrada do número informado é:", rai)


