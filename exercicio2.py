'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

val1 = int(input("Informe um valor inteiro: "))
val2 = int(input("Informe o segundo valor inteiro: "))
val3 = int(input("Informe o terceiro valor inteiro: "))
val4 = int(input("Informe o quarto valore inteiro: "))

adi = val1 + val2 + val3 + val4
mul = (val1 * val2) * (val3 * val4)

print("A soma de seus valores é", adi)
print("A multiplicação de seus valores é", mul)