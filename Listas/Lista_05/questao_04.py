nomes = []
idades = []
soma = 0

for i in range(6):
	nomes.append(input("Informe o nome: "))
	idades.append(int(input("Informe a idade: ")))
	soma += idades[i]

media = soma / (i + 1)

for i in range(6):
	if (idades[i] < media):
		print(nomes[i])