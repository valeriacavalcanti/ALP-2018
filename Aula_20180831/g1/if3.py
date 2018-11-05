nota1 = float(input())
nota2 = float(input())
frequencia = int(input())

media = (nota1 + nota2) / 2

print(media)


# verificar se está reprovado ou não

if (((media >= 70) and (frequencia >= 75)) or
    ((media >= 40) and (frequencia >= 75))):
    print ("Não está reprovado")
else:
    print("Reprovado")


if (((media >= 70) or (media >= 40)) and (frequencia >= 75)):
    print("Não está reprovado")
else:
    print("Reprovado")
