n = int(input())
b = 4
v = v1 = t = 1
lista = [1/4]
if n > 1:
    for i in range(0, n-1):
        if v == 0:
            t += 2
            b += 4
            lista.append(t/b)
            v += 1
        else:
            lista.append(1)
            v -= 1
    print(f'{sum(lista):.2f}')
    t = 1
    b = 4
    for i in range(1, n+1):
        if v1 == 1:
            if i == 1:
                print(f'{t}/{b}', end=' + ')
                t += 2
                b += 4
                v1 -= 1
            elif 1 < i < n:
                print(f'{t}/{b}', end=' + ')
                t += 2
                b += 4
                v1 -= 1
            else:
                print(f'{t}/{b}')
                t += 2
                b += 4
                v1 -= 1
        else:
            if 1 < i < n:
                print(1, end=' + ')
                v1 += 1
            else:
                print(1)
                v1 += 1
elif n == 1:
    print(0.25)
    print('1/4')
else:
    print(f'{0:.2f}')
