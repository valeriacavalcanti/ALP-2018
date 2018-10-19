lista = []
soma = 0
qtde = 0

for i in range(8):
	lista.append(int(input()))
	soma += lista[i]

media = soma / 8

for i in range(8):
	if (lista[i] > media):
		qtde += 1

print ("quantidade = %d" % qtde)