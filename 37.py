import numpy as np

def lista_rendezo(lista):
    atlag = np.average(lista)
    nulla = 0
    n = len(lista)
    i = 0
    while (i < n):
        if lista[i] < atlag:
            if lista[i] == 0:
                nulla += 1
            lista.remove(lista[i])
            n -= 1
        else:
            i += 1
    lista.sort()
    for i in range(nulla):
        lista.append(0)
    return lista

# lista=[7,10,0,9,11,0,17]
n = int(input('Elemszam: '))
lista = []
for i in range(n):
    a = int(input('Szam: '))
    lista.append(a)
print('Bemenet:', lista)
print('Kimenet:', lista_rendezo(lista))
