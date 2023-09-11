n = str(input()).split()
n1 = int(n[0])
n2 = int(n[1])
seq = list()

for i in range(0, n1):
    num = int(input())
    seq.append(num)
print(seq.count(n2))
