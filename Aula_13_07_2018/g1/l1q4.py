# IFPB
# Técnico em Informática
# Lista 01
# Questão 04
# 13/07/2018

numero = input("Informe um número: ")
numero = int(numero)

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

print("Centenas:",centenas)
print("Dezenas:",dezenas)
print("Unidades:",unidades)
