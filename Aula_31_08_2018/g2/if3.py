nota1 = float(input())
nota2 = float(input())
freq = int(input())

media = (nota1 + nota2) / 2

print("Media = %.2f" % media)


# verificar: ap, rep ou final

if ((media >= 70) and (freq >= 75)):
    print("Aprovado")
elif ((media >= 40) and (freq >= 75)):
    print("Final")
else:
    print("Reprovado")


# método natália

if (((media >= 70) and (freq >= 75)) or ((media >= 40) and (freq > 75))):
    print("Não está reprovado")
else:
    print("Reprovado")


# método laís maria

if (((media >= 70) or (media >= 40)) and (freq >= 75)):
    print("Não está reprovado")
else:
    print("Reprovado")


# método victor
if ((media >= 40) and (freq >= 75)):
    print("Não está reprovado")
else:
    print("Reprovado")

