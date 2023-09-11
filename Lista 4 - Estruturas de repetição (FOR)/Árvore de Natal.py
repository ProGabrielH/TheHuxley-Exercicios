n = float(input())
vt = 0

for i in range(0, 3):
    qnt = float(input())
    val = float(input())
    vt += qnt*val

print(f'{n+vt:.2f}')
print(f'{(n+vt)/21:.2f}')
