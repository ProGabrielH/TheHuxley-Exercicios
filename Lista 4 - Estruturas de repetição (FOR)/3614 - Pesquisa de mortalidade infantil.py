n = int(input())
s = 'n'
idade = 0
lists = list()
list_idade_m24 = list()
list_idade = list()

if n > 0:
    for i in range(0, n):
        sexo = str(input()).strip().lower()[0]
        lists.append(sexo)
        idade = int(input())
        if idade <= 24:
            list_idade_m24.append(idade)
        list_idade.append(idade)
    print(f'{((lists.count("f"))/len(lists))* 100:.1f}%')
    print(f'{((lists.count("m"))/len(lists))* 100:.1f}%')
    print(f'{(len(list_idade_m24)/len(list_idade))*100:.1f}%')

else:
    print('Informe um numero positivo')
