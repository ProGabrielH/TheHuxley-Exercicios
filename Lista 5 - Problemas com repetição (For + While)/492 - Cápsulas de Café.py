caps = 0

for i in range(0, 7):
    n = int(input())
    tam = str(input())
    if tam in 'Pp':
        caps += 10*n
    elif tam in 'Gg':
        caps += 16*n
print(caps)
print(f'{(caps*2)/7:.0f}')
