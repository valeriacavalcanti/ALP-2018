nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2

print("Media = %.2f" % media)


# forma 1

if (media >= 70):
    print("Aprovado")
else:
    if (media >= 40):
        print("Final")
    else:
        print("Reprovado")


# forma 2

if (media >= 70):
    print("Aprovado")
elif (media >= 40):
    print("Final")
else:
    print("Reprovado")
