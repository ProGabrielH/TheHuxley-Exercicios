print('Insira os valores das doacoes:')
soma = 0
cont = 0
div = 1

while True:
    n = float(input())
    if n < 0:
        break
    soma += n
    cont += 1
    if cont > 1:
        div += 1
print(f'Total arrecadado: {soma:.2f}')
print(f'Valor medio da doacao: {soma/div:.2f}')
