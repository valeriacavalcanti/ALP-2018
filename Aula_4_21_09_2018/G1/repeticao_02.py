quantidade = 0
soma = 0
soma_20 = 0

for i in range(4):
    num = int(input())
    soma = soma + num
    #print(i, num)
    if (num > 20):
        quantidade = quantidade + 1
        soma_20 = soma_20 + num

print("Quantidade =", quantidade)
print("Soma =", soma)
print("Soma acima de 20 =", soma_20)
print("Ultimo numero:", num)
print("i =", i)

media = soma / (i + 1)

if (quantidade > 0):
    media_20 = soma_20 / quantidade
    print("Media acima de 20 =", media_20)
print("Media =", media)

