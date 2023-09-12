litros = float(input())
combustivel = str(input()).strip().upper()

if combustivel == 'A':
    if litros <= 20:
        print(f'R$ {(litros*1.9)-(litros*1.9)*0.03:.2f}')
    else:
        print(f'R$ {(litros*1.9)-(litros*1.9)*0.05:.2f}')
elif combustivel == 'G':
    if litros <= 20:
        print(f'R$ {(litros*2.5)-(litros*2.5)*0.04:.2f}')
    else:
        print(f'R$ {(litros*2.5)-(litros*2.5)*0.06:.2f}')
elif combustivel == 'D':
    if litros <= 25:
        print(f'R$ {(litros*1.66):.2f}')
    else:
        print(f'R$ {(litros*1.66)-(litros*1.66)*0.04:.2f}')
