aprovados = 0

while True:
    qport = float(input())
    if qport < 0:
        break
    qmat = float(input())
    red = float(input())
    if (qport/50)*100 >= 80 and (qmat/35)*100 >= 60 and red >= 7:
        aprovados += 1
print(aprovados)
