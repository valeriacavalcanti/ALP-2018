senha = input("Senha: ")

if ((senha.isalnum() == True) and (len(senha) >= 4) and (len(senha) <= 10)):
  print("Senha válida")
else:
  print("Senha inválida")
