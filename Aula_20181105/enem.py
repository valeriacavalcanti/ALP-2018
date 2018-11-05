qt_sim = 0
qt_nao = 0
respostas = []
nomes = []
total = 0
p_sim = 0
p_nao = 0

nome = input("Qual é o seu nome?")
resposta = input(nome + ", você fez a prova?")
while (resposta == "SIM" or resposta == "NÃO"):
  nomes.append(nome)
  respostas.append(resposta)
  if (resposta == "SIM"):
    qt_sim += 1
  else:
    qt_nao += 1

  nome = input("Qual é o seu nome?")
  resposta = input(nome + ", você fez a prova?")

print("SIM = %d - NÃO = %d" % (qt_sim, qt_nao))
# print(respostas)

for i in range(len(respostas)):
  print("%s = %s" % (nomes[i], respostas[i]))

total = qt_sim + qt_nao
p_sim = (qt_sim * 100) / total
p_nao = (qt_nao * 100) / total

print("sim = %.1f %%" % p_sim)
print("não = %.1f %%" % p_nao)