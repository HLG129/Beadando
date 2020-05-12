import numpy as np

def negyzet(m):
    if m % 2 == 0:
        while m > 2:        #2 hatvanyaira all majd le
            m = m / 2
        if m == 2:
            return True
        return False


def csapatok(n):
    out_file = open('Agrajz.txt', 'w')
    mtx = np.zeros((n, n), dtype=int)
    for i in range(n):  #null matrix elso oszlopat feltolti a csapatok sorszamaval
        mtx[i,0] = i+1

    oszlop = 1
    masolat = n
    while oszlop < n:
        i = 1
        sor = 0
        while i < masolat:
            r = np.random.randint(0, 2)
            if r == 1:              #eldonti ki nyert
                mtx[sor,oszlop] = mtx[i,oszlop-1]
            else:
                mtx[sor,oszlop] = mtx[i-1,oszlop - 1]

            sor += 1
            i += 2
        oszlop += 1
        masolat //= 2

    #print(mtx)    #eddig nezi meg, hogy melyik csapat jut tovabb

    szoveg = ""
    tab = 3
    for i in range(n):
        szoveg += "Csapat{}\t".format(mtx[i,0])
    szoveg += "\n\t"
    for i in range(1, n):
        for j in range(n):
            if mtx[j,i] > 0:
                szoveg += "Csapat{}".format(mtx[j][i])
                for k in range(tab):
                    szoveg += "\t"

        szoveg += "\n"
        for k in range(tab):
            szoveg += "\t"

        tab += 4

    print(szoveg, file=out_file)
    out_file.close()


while True:
    n = int(input('Hany csapat van? (2 hatvanyszamait fogadom el) '))
    c=negyzet(n)
    if c:
        break

csapatok(n)
