nota1 = float(input())
nota2 = float(input())
frequencia = int(input())

media = (nota1 + nota2) / 2

print(media)


# verificar a média e a frequência

if ((media >= 70) and (frequencia >= 75)):
    print("Aprovado")
else:
    if ((media >= 40) and (frequencia >= 75)):
        print("Final")
    else:
        print("Reprovado")


# verificar apenas a média

if (media >= 70):
    print("Aprovado")
elif (media >= 40):
    print("Final")
else:
    print("Reprovado")
