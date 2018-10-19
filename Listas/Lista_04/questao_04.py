soma = 0

for i in range(6):
	num = int(input("Informe um número: "))
	soma += num

print("Média = %.2f" % (soma / (i + 1)))