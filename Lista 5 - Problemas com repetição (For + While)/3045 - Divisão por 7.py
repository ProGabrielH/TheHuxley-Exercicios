n = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n % 7 == 0:
        print('S')
    else:
        print('N')
