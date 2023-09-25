from math import sqrt

lado = float(input())
print(f'Lado do hexagono: {lado:.1f} metros,')
print(f'Area: {((pow(lado, 2)*sqrt(3))/4)*6} metros quadrados,')
print(f'Perimetro: {lado*6:.1f} metros.')
