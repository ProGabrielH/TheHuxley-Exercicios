n = float(input())
e = int(input())
exp = 1

for i in range(0, e):
    exp *= n

print(f'{exp:.2f}')
