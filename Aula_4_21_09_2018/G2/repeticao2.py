
quantidade = 0
soma = 0
soma_20 = 0

for i in range(4):
    num = int(input())
    soma = soma + num
    if (num > 20):
        quantidade = quantidade + 1
        soma_20 = soma_20 + num
        
    print(i + 1, num)

print("i =", i)
print("num = ", num)
print("quantidade =", quantidade)
print("soma =", soma)
print("soma acima de 20 = ", soma_20)

media = soma / (i + 1)

if (quantidade > 0):
    media_20 = soma_20 / quantidade
    print("media acima de 20 =", media_20)

print("media =", media)
