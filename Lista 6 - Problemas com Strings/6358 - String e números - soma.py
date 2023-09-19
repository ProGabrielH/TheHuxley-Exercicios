n1 = input()
n2 = input()
erro = 0

for i in n1.split():
    if int(i) > 9:
        erro += 1
for k in n2.split():
    if int(k) > 9:
        erro += 1

if erro == 0:
    n1 = n1.replace(' ', '')
    n2 = n2.replace(' ', '')
    snum = int(n1) + int(n2)
    for l, j in enumerate(str(snum)):
        if l < len((str(snum))) - 1:
            print(j, end=' ')
        else:
            print(j)
else:
    print('Erro em uma ou mais sequencia de entrada de dados')
