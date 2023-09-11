n = int(input())

for i in range(1, n+1):
    for p in range(1, i+1):
        if p == i:
            print(p, end='')
        else:
            print(p, end=' ')
    print('')
