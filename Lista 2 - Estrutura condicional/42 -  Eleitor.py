idade = int(input())

if idade < 16:
    print('nao eleitor')
elif 16 <= idade < 18 or idade > 65:
    print('eleitor facultativo')
elif 18 <= idade <= 65:
    print('eleitor obrigatorio')
