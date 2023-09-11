while True:
    ph = float(input())
    if ph < 7 and ph > 0:
        print('ACIDA')
    elif ph > 7:
        print('BASICA')
    elif ph == 7:
        print('NEUTRA')
    if ph < 0:
        break
