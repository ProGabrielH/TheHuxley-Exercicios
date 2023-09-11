n = int(input())
p = int(input())

if p != 0:
    for i in range(n+p, n+(p*4), p):
        print(i, end=' ')
else:
    for i in range(0, 3):
        print(n, end=' ')
        