palavra = input()

while palavra != 'FIM':
    for i in palavra:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'o', 'O', 'l']:
            print('ERRO')
            break
    else:
        palavra = palavra.replace('l', '1')
        palavra = palavra.replace('O', '0')
        palavra = palavra.replace('o', '0')
        palavra = palavra.lstrip('0')
        print(palavra)
    palavra = input()
