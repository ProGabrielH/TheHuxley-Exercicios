qnt = int(input())
fila = list(input().lower().split())
fichas = 20 - fila.count('d')
a = d = um = tam = 0


if fichas > 0:
    for i in fila:
        if fichas == 0:
            break
        else:
            if i == 'a':
                fichas -= 1
                um = tam
            tam += 1
    print(um)
else:
    print(-1)
