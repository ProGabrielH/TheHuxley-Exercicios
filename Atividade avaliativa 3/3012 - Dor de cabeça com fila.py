pessoas = list(input().split())
pessoasRemover = list(input().split())
confirmador = 0

if len(pessoas) <= 0:
    print('Fila de entrada vazia')
else:
    if len(pessoasRemover) >= len(pessoas):
        print('Fila de saida maior que a de entrada')
    else:
        for k, i in enumerate(pessoasRemover):
            if i in pessoas:
                pessoas.remove(i)
            else:
                confirmador += 1
        if confirmador > 0:
            print('Impossivel tirar pessoa inexistente da fila')
        else:
            for c, j in enumerate(pessoas):
                if c < len(pessoas)-1:
                    print(j, end=' ')
                else:
                    print(j, end='')
