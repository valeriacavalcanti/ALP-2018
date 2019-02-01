frase = "Que bom!"
frase += " "
frase += "Hoje é sexta!"
letra = "aeiou"
numero = "0123456789"
letra_num = letra + numero
especiais = letra + "@" +numero
palavra = "oi"

print(frase)
print(frase.split())
print(frase.count("e"))
print(frase.find("sexta"))
print(frase.find("oi"))
print(frase.replace("sexta", "sábado"))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.swapcase())

print(letra)
print(numero)
print(letra_num)
print(especiais)

print(letra.isalpha())
print(numero.isalpha())
print(letra_num.isalpha())
print(especiais.isalpha())

print(letra.isdigit())
print(numero.isdigit())
print(letra_num.isdigit())
print(especiais.isdigit())

print(letra.isalnum())
print(numero.isalnum())
print(letra_num.isalnum())
print(especiais.isalnum())

print(frase.isspace())
print("        ".isspace())

print("[",palavra,"]")

print("[",palavra.ljust(10),"]")
print("[",palavra.rjust(10),"]")
print("[",palavra.center(10),"]")