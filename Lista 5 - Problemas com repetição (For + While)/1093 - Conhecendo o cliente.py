resp = 'S'
vendas_vista = list()
vendas_cartao = list()
vendas = list()
idades = list()


while resp in 'Ss':
    idade = int(input())
    idades.append(idade)
    valor = float(input())
    vendas.append(valor)
    pag = str(input()).upper().strip()[0]
    if pag in 'Cc':
        vendas_cartao.append(valor)
    elif pag in 'Vv':
        vendas_vista.append(valor)
    resp = str(input()).upper().strip()[0]

print(len(vendas))
if len(vendas_vista) == 0:
    print(0)
else:
    print(f'{sum(vendas_vista):.2f}')
if len(vendas_cartao) == 0:
    print(0)
else:
    print(f'{sum(vendas_cartao):.2f}')
print(min(idades))
print(f'{max(vendas):.2f}')
if len(vendas_vista) == 0:
    print(0)
else:
    print(f'{sum(vendas_vista)/len(vendas_vista):.2f}')
