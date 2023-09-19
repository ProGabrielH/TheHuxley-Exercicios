n = int(input())

for i in range(n):
    frase = input().replace(' ', '').lower()
    if frase == frase[::-1]:
        print('SIM')
    else:
        print('NAO')
