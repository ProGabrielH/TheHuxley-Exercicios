tipo = str(input()).strip().upper()
valor = float(input())
if tipo != 'PPF' and tipo != 'PPJ' and tipo != 'PP':
    print('Despesa inv�lida.')
else:
    if tipo == 'PP':
        if valor > 4000:
            print('Excesso de pagamento para pessoal.')
        else:
            print('Pagamento liberado.')
    else:
        rubrica = str(input()).strip().upper()

        if tipo == 'PPF':
            if rubrica != 'SERV':
                print('Pessoa f�sica n�o pode fornecer materiais para o servi�o p�blico.')
            elif valor > 8000:
                print('Excesso de pagamento para pessoa f�sica.')
            else:
                print('Pagamento liberado.')
        if tipo == 'PPJ':
            if rubrica == 'CAP':
                if valor <= 5000000:
                    print('Pagamento liberado.')
                else:
                    print('O valor para pagamento da rubrica de capital n�o pode exceder R$ 5M.')
            elif rubrica == 'CUST':
                if valor <= 2000000:
                    print('Pagamento liberado.')
                else:
                    print('O valor para pagamento da rubrica de custeio n�o pode exceder R$ 2M.')
            elif rubrica == 'SERV':
                if valor <= 500000:
                    print('Pagamento liberado.')
                else:
                    print('O valor para pagamento da rubrica de servi�os n�o pode exceder R$ 500K.')