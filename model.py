import random
import json

# Definirajmo konstante
VRSTICE = 4
STOLPCI = 6
VELIKOST_IGRALNE_PLOSCE = VRSTICE * STOLPCI

#ZACETEK = 'S'
#ZMAGA = 'W'
#PORAZ = 'L'

LAHKA_TEZAVNOST = 2
SREDNJA_TEZAVNOST = 3
TEZKA_TEZAVNOST = 4

SEZNAM_CRK = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# Definirajmo logicni model igre
class Memory: 

    def __init__(self, tezavnost): # igra je definirana s tezavnostjo (t.j. koliko polj steje za "par")
        self.tezavnost = tezavnost
        self.crke = SEZNAM_CRK[:(VELIKOST_IGRALNE_PLOSCE // self.tezavnost)] * self.tezavnost
        random.shuffle(self.crke)
        self.skrita = [list('*' * STOLPCI) for i in range(VRSTICE)] #na zacetku igre potrebujemo prazno ploso
        self.zadnji_ugib = []
        self.plosca = [self.crke[:6],
                    self.crke[6:12],
                    self.crke[12:18],
                    self.crke[18:24]]
        return

    def pokazi(self):
        # pokaze nas trenutni rezultat
        niz = ""
        for i in range(0, VRSTICE):
            for j in range(0, STOLPCI):
                niz = niz + self.skrita[i][j] + " "
            if i != VRSTICE - 1:
                niz = niz + "\n"
        print(niz)

    def ugibaj(self, seznam): 
        # seznam je seznam ugibov, to je [[x1, y1], [x2, y2]]
        self.zadnji_ugib = seznam
        if self.tezavnost == 2:
            par_1 = seznam[0]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = seznam[1]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            if ugib1 == ugib2:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
                return 1
            return 0
        elif self.tezavnost == 3:
            par_1 = seznam[0]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = seznam[1]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            par_3 = seznam[2]
            ugib3 = self.plosca[par_3[0]][par_3[1]]
            if ugib1 == ugib2 and ugib2 == ugib3:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
                self.skrita[par_3[0]][par_3[1]] = ugib3
                return 1
            return 0
        elif self.tezavnost == 4:
            par_1 = seznam[0]
            ugib1 = self.plosca[par_1[0]][par_1[1]]
            par_2 = seznam[1]
            ugib2 = self.plosca[par_2[0]][par_2[1]]
            par_3 = seznam[2]
            ugib3 = self.plosca[par_3[0]][par_3[1]]
            par_4 = seznam[3]
            ugib4 = self.plosca[par_4[0]][par_4[1]]
            if ugib1 == ugib2 and ugib2 == ugib3 and ugib3 == ugib4:
                self.skrita[par_1[0]][par_1[1]] = ugib1
                self.skrita[par_2[0]][par_2[1]] = ugib2
                self.skrita[par_3[0]][par_3[1]] = ugib3
                self.skrita[par_4[0]][par_4[1]] = ugib4

        else:
            print('Vnesi veljavno tezavnost (2, 3 ali 4)!')

    def zmaga(self):
        if self.skrita == self.plosca:
            return True
        return False
    
#----------------------------------------------------------------------------------------------------------------------------#

#tekstovni vmesnik za class Memory

class Igra:
    def __init__(self):
        tezavnost = int(input(""" "Izberi tezavnost (lahko = 2, srednje = 3, tezko = 4): """))
        if tezavnost not in [2, 3, 4]:
            print("Nisi uposteval navodil!!! \n Vnesi veljaven vnos!!!")
            raise ValueError()
        else:
            if tezavnost == 2:
                self.game = Memory(2)
            elif tezavnost == 3:
                self.game = Memory(3)
            else:
                self.game = Memory(4)
        self.game.pokazi()
        while self.game.zmaga() != True:
            print("Izberi polja, t.j. vrstica (med 0 in 3), stolpec (med 0 in 5). Primer: polje 1: 1,2")
            # t.j. vnos pricakujemo kot 3,4 ali 1,1 (vnos je avtomatsko niz)
            if tezavnost == 2:
                p1 = input("Polje 1 (0-3,0-5): ")
                p2 = input("Polje 2 (0-3,0-5): ")
                while p1 == p2:
                    print('Napaka!!! Vnesi veljaven vnos!')
                    p1 = input("Polje 1 (0-3,0-5): ")
                    p2 = input("Polje 2 (0-3,0-5): ")
                sez = [[int(p1[0]), int(p1[2])], [int(p2[0]), int(p2[2])]]
            elif tezavnost == 3:
                p1 = input("Polje 1 (0-3,0-5): ")
                p2 = input("Polje 2 (0-3,0-5): ")
                p3 = input("Polje 3 (0-3,0-5): ")
                while p1 == p2 or p2 == p3 or p1 == p3:
                    print('Napaka!!! Vnesi veljaven vnos!')
                    p1 = input("Polje 1 (0-3,0-5): ")
                    p2 = input("Polje 2 (0-3,0-5): ")
                    p3 = input("Polje 3 (0-3,0-5): ")
                sez = [[int(p1[0]), int(p1[2])], [int(p2[0]), int(p2[2])], [int(p3[0]), int(p3[2])]]
            else:
                p1 = input("Polje 1 (0-3,0-5): ")
                p2 = input("Polje 2 (0-3,0-5): ")
                p3 = input("Polje 3 (0-3,0-5): ")
                p4 = input("Polje 4 (0-3,0-5): ")
                while p1 == p2 or p2 == p3 or p3 == p4 or p1 == p4:
                    print('Napaka!!! Vnesi veljaven vnos!')
                    p1 = input("Polje 1 (0-3,0-5): ")
                    p2 = input("Polje 2 (0-3,0-5): ")
                    p3 = input("Polje 3 (0-3,0-5): ")
                    p4 = input("Polje 4 (0-3,0-5): ")
                sez = [[int(p1[0]), int(p1[2])], [int(p2[0]), int(p2[2])], [int(p3[0]), int(p3[2])], [int(p4[0]), int(p4[2])]]
            self.game.ugibaj(sez)
            niz1 = "Izbor:"
            for par in self.game.zadnji_ugib:
                niz1 = niz1 + " {0},{1} = {2} ;".format(par[0], par[1], self.game.plosca[par[0]][par[1]])
            print(niz1)
            self.game.pokazi()
        print("ZMAGA!")

#----------------------------------------------------------------------------------------------------------------------------#


        
        
        
        

