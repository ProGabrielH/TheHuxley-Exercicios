x = input().split()
n = int(x[0])
m = int(x[1])
menorTempo = float('inf')
melhorAluno = 0

for i in range(0, n):
    array = [int(x) for x in input().split()]
    if sum(array) < menorTempo:
        menorTempo = sum(array)
        melhorAluno = i+1

print(melhorAluno)
