frase = input("Frase: ")
palavra = input("Palavra: ")


# forma 1
if (frase.count(palavra) > 0):
  print("Existe!")
else:
  print("Não existe!")


# forma 2
if (frase.find(palavra) != -1):
  print("Existe!")
else:
  print("Não existe!")