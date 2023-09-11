n = int(input())
soma = 0
if n > 0:
    for i in range(1, n):
        soma += i/(i*3)
        print(f'{i}/{3*i} + ', end='')
    print(f'{n}/{n*3}')
    soma += n/(n*3)
    print(f'{soma:.2f}')
else:
    print(f'{0:.2f}')
