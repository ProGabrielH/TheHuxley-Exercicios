cinema = 0
boliche = 0
for i in range(0, 6):
    voto = input().lower().strip()
    if voto == 'cinema':
        cinema += 1
    else:
        boliche += 1
if cinema > boliche:
    print('CINEMA')
else:
    print('BOLICHE')
