while True:
    n = int(input())
    if n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        break
    else:
        print('Insira um número inicial entre 1 e 9')

while True:
    n2 = int(input())
    if n2 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        break
    else:
        print('Insira um número final entre 1 e 9')
if n > n2:
    print('Nenhuma tabuada nesse intervalo')
while n <= n2:
    for i in range(1, 10):
        print(f'{n} x {i} = {n*i}')
    n += 1
    print('')
