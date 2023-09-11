n = input()
n = n.split()
ni = int(n[0])
nf = int(n[1])
t = 0

for i in range(ni, nf+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
        t += 1
if t == 0:
    print("-1")
print('\n')
