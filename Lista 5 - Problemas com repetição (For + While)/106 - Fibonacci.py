n1, n2 = 0, 1
termos = int(input())

while termos != 0:
    for i in range(0, termos):
        if i < termos-1:
            print(n1, end=' ')
        else:
            print(n1, end='')
        nn2 = n1 + n2
        n1 = n2
        n2 = nn2
    n1, n2 = 0, 1
    print('')
    termos = int(input())
