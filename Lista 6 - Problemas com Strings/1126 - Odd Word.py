texto = input().split()
for k, i in enumerate(texto):
    if (k+1) < len(texto):
        if (k+1) % 2 == 0:
            print(i[::-1], end=' ')
        else:
            print(i, end=' ')
    else:
        if (k+1) % 2 == 0:
            print(i[::-1], end='')
        else:
            print(i, end='')
