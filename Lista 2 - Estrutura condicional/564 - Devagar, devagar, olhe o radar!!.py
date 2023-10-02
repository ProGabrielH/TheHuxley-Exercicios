velocidadeMaxima = float(input())
velocidadeMotorista = float(input())

if velocidadeMaxima < velocidadeMotorista <= velocidadeMaxima + (velocidadeMaxima*0.2):
    print(85.13)
    print(4)
elif velocidadeMaxima + (velocidadeMaxima*0.2) < velocidadeMotorista <= velocidadeMaxima + (velocidadeMaxima*0.5):
    print(127.69)
    print(5)
elif velocidadeMaxima + (velocidadeMaxima*0.5) < velocidadeMotorista:
    print(574.62)
    print(7)
else:
    print(f'{0:.2f}')
    print(0)
