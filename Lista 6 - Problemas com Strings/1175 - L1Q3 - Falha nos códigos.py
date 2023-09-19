codigoPokemon = input()

if codigoPokemon[6] in 'Bb':
    print('Bulbassauro')
elif codigoPokemon[6] in 'Cc':
    print('Charmander')
elif codigoPokemon[6] in 'Ss':
    print('Squirtle')
else:
    print('Codigo Invalido')
