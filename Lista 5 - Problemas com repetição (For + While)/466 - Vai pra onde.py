cidade = input().upper()
array = ["", None, None]

while(cidade != "FIM"):
    km = int(input())
    passagem = float(input())
    passagem *= 2
    if(array[1] is None):
        if(passagem <= 300):
            array[1] = km
            array[2] = passagem
            array[0] = cidade
    elif(passagem <= 300 and array[1] < km):
            array[1] = km
            array[2] = passagem
            array[0] = cidade
    cidade = input().upper()

if(array[0] == ""):
    print("SEM DESTINO")
else:
   print(array[0])
