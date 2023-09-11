idades = list()

for i in range(0, 100):
    n = int(input())
    idades.append(n)
print(f'mais novo: {min(idades)}')
print(f'mais velho: {max(idades)}')
