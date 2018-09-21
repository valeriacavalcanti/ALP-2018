# 1051

salario = float(input())

if (salario <= 2000):
    print("Isento")
elif (salario <= 3000):
    imposto = (salario - 2000) * 0.08
    print("R$ %.2f" % imposto)
elif (salario <= 4500):
    imposto = 80 + (salario - 3000) * 0.18
    print("R$ %.2f" % imposto)
else:
    imposto = 80 + 270 + (salario - 4500) * 0.28
    print("R$ %.2f" % imposto)
