array1 = []
array2 = []
qnt1 = int(input())
if qnt1 < 1:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
else:
    for i in range(0, qnt1):
        array1.append(input())
    qnt2 = int(input())
    if qnt2 < 1:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
    else:
        for i in range(0, qnt2):
            array2.append(input())
        for i in array1:
            print(i, end=' ')
        for k, i in enumerate(array2):
            if k < len(array2)-1:
                print(i, end=' ')
            else:
                print(i, end='')
