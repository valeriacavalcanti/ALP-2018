maior = int(input("Informe um número: "))

for i in range(7):
	num = int(input("Informe um número: "))
	if (num > maior):
		maior = num

print("Maior = %d" % maior)