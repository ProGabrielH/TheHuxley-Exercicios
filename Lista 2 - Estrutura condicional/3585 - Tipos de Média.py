tipo = str(input()).strip().lower()
n1 = float(input())
n2 = float(input())
n3 = float(input())
if tipo not in 'aph':
    print('Caractere invalido')
else:
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        print('Notas erradas')
    else:
        if tipo == 'a':
            m = (n1+n2+n3)/3
            print(f'{m:.2f}')
            if 7 <= m <= 10:
                print('Aprovado')
            elif 0 <= m <= 4:
                print('Reprovado')
            else:
                print('Prova final')
        elif tipo == 'p':
            p1 = float(input())
            p2 = float(input())
            p3 = float(input())
            m = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
            print(f'{m:.2f}')
            if 7 <= m <= 10:
                print('Aprovado')
            elif 0 <= m <= 4:
                print('Reprovado')
            else:
                print('Prova final')
        elif tipo == 'h':
            m = 3/((1/n1)+(1/n2)+(1/n3))
            print(f'{m:.2f}')
            if 7 <= m <= 10:
                print('Aprovado')
            elif 0 <= m <= 4:
                print('Reprovado')
            else:
                print('Prova final')
