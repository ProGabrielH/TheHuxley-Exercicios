mincre = 15
minmat = '123'
sum = 0
cqnt = 0

while True:
    mat = str(input())
    if mat == '999':
        break
    cre = float(input())
    cqnt += 1
    sum += cre
    if cre < mincre:
        mincre = cre
        minmat = mat
print(minmat)
print(f'{sum/cqnt:.2f}')
