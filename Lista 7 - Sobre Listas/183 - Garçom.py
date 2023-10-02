bandeijas = int(input())
latas = []
copos = []
quebrou = 0

for i in range(0, bandeijas):
    x = input().split()
    latas.append(int(x[0]))
    copos.append((int(x[1])))

for k in range(0, bandeijas):
    if latas[k] > copos[k]:
        quebrou += copos[k]
print(quebrou)
