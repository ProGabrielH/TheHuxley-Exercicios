espaco = input().strip().upper()
mala = input().strip().upper()
valor = float(input())
motor = float(input())
cambio = input().strip().upper()
pontos = 0

if espaco != 'A' or mala != 'G':
    print('N�o compre!')
else:
    if valor < 100000:
        pontos += 1
    if motor >= 1.5:
        pontos += 1
    if cambio in 'Aa':
        pontos += 1
    if pontos <= 0:
        print('Recomendo pensar melhor...')
    elif pontos == 1:
        print('Pode ser uma op��o.')
    elif pontos == 2:
        print('Boa compra.')
    else:
        print('Pode comprar!')
