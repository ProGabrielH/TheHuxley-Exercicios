dna = input().upper()
base = input().upper()
pos = 0
subs = ''
tempSubs = ''

if base not in dna:
    print('ERRO')
else:
    for n, i in enumerate(dna):
        if i == base:
            tempSubs += i
            if len(tempSubs) > len(subs):
                subs = ''
                pos = n
                subs += tempSubs
        else:
            tempSubs = ''
            tempPos = 0

    print(pos - (len(subs)-1))
    print(len(subs))

