d1 = int(input())
d2 = int(input())
m = int(input())

f = float(10*m/(d1+d2))
print(f'Scar conseguiu criar uma frustra��o {f:.2f} na turma')
if f >= 4:
    print('Eu matei Mufasa')
elif f <= 2:
    print('Mais um fracasso...')
elif 2 < f < 4:
    print('Consegui lacaios preciosos')
