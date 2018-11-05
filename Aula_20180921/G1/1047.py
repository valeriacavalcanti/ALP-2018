# 1047

hi, mi, hf, mf = input().split(" ")
hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)

tempoi = (hi * 60) + mi
tempof = (hf * 60) + mf

if (tempoi == tempof):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif (tempoi < tempof):
    duracao = tempof - tempoi
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao//60, duracao%60))
else:
    duracao = ((24 * 60) - tempoi) + tempof
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao//60, duracao%60))
    
