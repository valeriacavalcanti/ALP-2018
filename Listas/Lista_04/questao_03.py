qtde = 0

for i in range(6):
	num = int(input("Informe um número: "))
	if (num > 100):
		qtde += 1

print("Quantidade = %d" % qtde)