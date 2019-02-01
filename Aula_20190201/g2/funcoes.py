def ma(p1, p2, p3):
  media = (p1 + p2 + p3)/3
  return media

def mp(p1, p2, p3):
  media = ((p1 * 3) + (p2 * 3) + (p3 * 4))/10
  return media

def escolha(p1, p2, p3):
  m_arit = ma(p1, p2, p3)
  m_pond = mp(p1, p2, p3)
  if (m_arit > m_pond):
    return "Média arit"
  elif (m_arit < m_pond):
    return "Média pond"
  else:
    return "Tanto Faz!"

def fome():
  print("estou com fome")
  print("quero pastel")
  print("pode ser tapioca")
  print("quero ir para casa")
  print("bom final de semana!")


# código principal
v1, v2, v3 = input().split()
v1, v2, v3 = float(v1), float(v2), float(v3)

print(ma(v1, v2, v3))
print(mp(v1, v2, v3))
print(escolha(v1, v2, v3))

print(ma(v1, v2, v3))
print(ma(v1, v2, v3))
print(ma(v1, v2, v3))
print(ma(v1, v2, v3))
print(ma(v1, v2, v3))

fome()