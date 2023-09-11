n = int(input())
cont = 0

for i in range(1, n+1):
    if (i-1) * i * (i+1) == n:
        print(f'{i-1} * {i} * {i+1} = {n}')
        print('Verdadeiro')
        cont += 1
        break
if cont == 0:
    print('Falso')
