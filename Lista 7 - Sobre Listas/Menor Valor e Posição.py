qnt = input()
array = [int(x) for x in input().split()]

print(f'Menor valor: {min(array)}')
print(f'Posicao: {array.index(min(array))}')
