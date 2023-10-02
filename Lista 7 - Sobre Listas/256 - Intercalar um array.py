tamanho = int(input())
array1 = []
array2 = []
novoArray = []
interlacador = 0

for i in range(0, tamanho):
    array1.append(input())
for i in range(0, tamanho):
    array2.append(input())

for i in range(0, tamanho):
    novoArray.append(array1[i])
    novoArray.append(array2[i])

for i in novoArray:
    print(i)
