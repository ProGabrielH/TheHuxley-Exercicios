n = int(input())
p = int(input())
v = 0

for i in range(0, n):
    n1 = int(input())
    n2 = int(input())
    if n1 != 0 and n2 != 0:
        if n1 + n2 >= p:
            v += 1
print(v)
