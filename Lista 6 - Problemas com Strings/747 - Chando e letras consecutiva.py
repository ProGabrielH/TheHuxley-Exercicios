n = int(input())
gs = list()

for i in range(0, n):
    t = input()
    gs.append(t[0])
    for v in t:
        if v != gs[-1]:
            gs.append(v)
    for k in gs:
        print(k, end='')
    print('')
    gs.clear()
