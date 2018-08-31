# Avaliação 2
# Questão 1

tempo = int(input())

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60

print(horas, minutos, segundos, sep=":")

print("%d:%d:%d" % (horas, minutos, segundos))
