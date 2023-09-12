ph = int(input('Digite o pH da solucao:'))

if 7 < ph < 14:
    print('\nEssa solucao e basica.')
elif 0 < ph < 7:
    print('\nEssa solucao e acida.')
elif ph == 7:
    print('\nEssa solucao e neutra.')
else:
    print('\nValor deve estar entre 0 e 14.')
