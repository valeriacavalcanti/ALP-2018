qt_sim = 0
qt_nao = 0
respostas = []
nomes = []
total = 0
p_sim = 0
p_nao = 0

nome = input("Qual � o seu nome?")
resposta = input(nome + ", voc� fez a prova?")
while (resposta == "SIM" or resposta == "N�O"):
  nomes.append(nome)
  respostas.append(resposta)
  if (resposta == "SIM"):
    qt_sim += 1
  else:
    qt_nao += 1

  nome = input("Qual � o seu nome?")
  resposta = input(nome + ", voc� fez a prova?")

print("SIM = %d - N�O = %d" % (qt_sim, qt_nao))
# print(respostas)

for i in range(len(respostas)):
  print("%s = %s" % (nomes[i], respostas[i]))

total = qt_sim + qt_nao
p_sim = (qt_sim * 100) / total
p_nao = (qt_nao * 100) / total

print("sim = %.1f %%" % p_sim)
print("n�o = %.1f %%" % p_nao)