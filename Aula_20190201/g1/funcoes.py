def boas_vindas():
  print("Bom dia!! Hoje é sexta!!")
  print("O dia está muito lindo!!")
  print("Amanhã é sábado!!")
  print("Hoje tem prova de Fabrízia!!")
  print("Que bom!")

def ma(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3)/3
  return media

def mp(nota1, nota2, nota3):
  media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10
  return media

def melhor(nota1, nota2, nota3):
  media_a = ma(nota1, nota2, nota3)
  media_p = mp(nota1, nota2, nota3)
  if (media_a > media_p):
    return "Média Aritmética"
  elif (media_a < media_p):
    return "Média Ponderada"
  else:
    return "Tanto Faz"

# Programa Principal
boas_vindas()
n1, n2, n3 = input().split()
n1, n2, n3 = float(n1), float(n2), float(n3)
print(ma(n1, n2, n3))
print(mp(n1, n2, n3))
print(melhor(n1, n2, n3))
