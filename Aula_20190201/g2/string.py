frase = "Eu quero tapioca"

vogais = "aeiou"
numeros = "0123456789"
letras_numeros = vogais + numeros
especiais = vogais + "@" + numeros

palavra = "oi"

print(frase)
print(frase.split())
print(frase.split("quero"))
print(frase.count("a"))
print(frase.find("eita"))
print(frase.replace("tapioca", "pastel"))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.swapcase())

print("# isalpha")
print(vogais.isalpha())
print(numeros.isalpha())
print(letras_numeros.isalpha())
print(especiais.isalpha())

print("# isdigit")
print(vogais.isdigit())
print(numeros.isdigit())
print(letras_numeros.isdigit())
print(especiais.isdigit())

print("# isalnum")
print(vogais.isalnum())
print(numeros.isalnum())
print(letras_numeros.isalnum())
print(especiais.isalnum())

print("# isspace")
print("".isspace())
print(" ".isspace())
print("        ".isspace())

print("[", palavra, "]")
print("[", palavra.ljust(10), "]")
print("[", palavra.rjust(10), "]")
print("[", palavra.center(10), "]")