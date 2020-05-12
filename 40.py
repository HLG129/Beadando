import numpy as np

def szokitalalo(m):
    global nyeresek_szama
    n = np.random.randint(1, 100)
    #print(n)
    i = 0
    while (i < m):
        k = int(input('Melyik szamra gondoltam? '))
        if k > n:
            print('Kisebbre')
        elif k < n:
            print('Nagyobbra')
        else:
            print('Talalt!')
            nyeresek_szama += 1
            break
        i += 1
    if i==m:
        print('Nem sikserult eltalani!')

def fajlkezelo(my_file):
    out_file = open('Score.txt', 'w')
    print('Megnyert jatekok szama: ', nyeresek_szama, file=out_file)
    out_file.close()

my_file = open("Score.txt", "w")
valasztas = 0
nyeresek_szama = 0

while True:
    print("""
1.New Game
2.Score
3.Difficulty
4.Quit""")
    ans = input("\nMit szeretne csinalni? ")
    if ans == "1":
        if valasztas == 0:
            print('{} probalkozasa van'.format(10))
            szokitalalo(10)
        else:
            print('{} probalkozasa van'.format(valasztas))
            szokitalalo(valasztas)

    elif ans == "2":
        print("\nAz eddig megnyert jatekait a Score fulon tudja megtekinetni")
        fajlkezelo(my_file)
    elif ans == "3":
        print("""
1.Konnyu
2.Kozepes
3.Nehez""")
        tmp = input("\nMilyen nehezet szeretne jatszani? ")
        if tmp == '1':
            print('\n10-szer probalkozhat')
            valasztas = 10
        elif tmp == '2':
            print('\n7-szor probalkozhat')
            valasztas = 7
        elif tmp == '3':
            print('\n4-szer probalkozhat')
            valasztas = 4
        else:
            print('\nNincs ilyen menupont')

    elif ans == "4":
        print("\n Goodbye!")
        break
    else:
        print("\nNincs ilyen menupont")

my_file.close()