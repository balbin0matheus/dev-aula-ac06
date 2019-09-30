numero = int(input("Digite o range dos numeros: "))

cont = 1
listaPrimos = []
while True:
    if cont > 1:
        for i in range(2,cont):
            if (cont % i) == 0:
                break
        else:
            listaPrimos.append(cont)
    if (len(listaPrimos) == numero):
        print(listaPrimos)
        break
    else:
        cont = cont + 1
        continue