c9 = c4 = c5 = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n == 9:
        c9 += 1
    elif n == 4:
        c4 += 1
    elif n == 5:
        c5 += 1
lista = {9: c9, 4: c4, 5: c5}
slista = sorted(lista.items(), key=lambda x:x[1])
print(f'canal {slista[2][0]}: {slista[2][1]}')
print(f'canal {slista[1][0]}: {slista[1][1]}')
print(f'canal {slista[0][0]}: {slista[0][1]}')
