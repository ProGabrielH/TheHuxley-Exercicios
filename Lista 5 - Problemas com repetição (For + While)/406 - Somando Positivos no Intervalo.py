n1 = int(input())
n2 = int(input())
soma = 0
if n2 > n1:
    if n2 > 0:
        soma += n2
    for i in range(n1, n2):
        if i > 0:
            soma += i
else:
    if n1 > 0:
        soma += n1
    for i in range(n2, n1):
        if i > 0:
            soma += i
print(soma)
