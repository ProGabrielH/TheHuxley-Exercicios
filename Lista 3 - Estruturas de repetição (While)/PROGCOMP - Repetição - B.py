qntn = 0
sumn = 0

while True:
    n = int(input())
    if n == 0:
        break
    qntn += 1
    sumn += n
print(int(sumn/qntn))
