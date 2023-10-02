numero = int(input())
notas = []

if 0 < numero <= 5:
    for i in range(0, numero):
        notas.append(float(input()))
    for k, i in enumerate(notas):
        print(f'Nota {k+1}: {i:.1f}')
    print(f'Media: {sum(notas)/len(notas):.2f}')
else:
    print('Numero de notas invalido.')
