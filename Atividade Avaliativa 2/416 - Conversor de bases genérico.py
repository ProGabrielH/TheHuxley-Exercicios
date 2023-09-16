qnt = int(input())
lista = list()

for i in range(0, qnt):
    n = int(input())
    base = int(input())
    if base == 16:
        print(hex(n).upper()[2:])
    elif base == 10:
        print(n)
    else:
        while True:
            if n < base:
                if n == 10:
                    lista.append('A')
                elif n == 11:
                    lista.append('B')
                elif n == 12:
                    lista.append('C')
                elif n == 13:
                    lista.append('D')
                elif n == 14:
                    lista.append('E')
                elif n == 15:
                    lista.append('D')
                else:
                    lista.append(n % base)
                break
            else:
                k = int(n % base)
                if k == 10:
                    lista.append('A')
                elif k == 11:
                    lista.append('B')
                elif k == 12:
                    lista.append('C')
                elif k == 13:
                    lista.append('D')
                elif k == 14:
                    lista.append('E')
                elif k == 15:
                    lista.append('D')
                else:
                    lista.append(k)
                n //= base
        lista_revertida = reversed(lista)

        for j in lista_revertida:
            print(j, end='')
        lista.clear()
        print('')

# Maneira mais otimizada e simples de fazer:
#
# def dec2any(dec,base_final):
#    base_final = int(base_final)
#    dec = int(dec)
#    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
#    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#    numero_final_temp = []
#    numero_final = ''
#    while True:
#        temp_numero_final = dec%base_final
#        numero_final_temp.append(temp_numero_final)
#        if int(dec/base_final) == 0:
#            break
#        dec = int(dec/base_final)
#    numero_final_temp.reverse()
#    for i in numero_final_temp:
#        numero_final += dic[i]
#    return numero_final
