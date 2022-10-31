class Hissi:
    def __init__(self, alin, ylin, atm):
        self.alin = alin
        self.ylin = ylin
        self.atm = atm

    def siirry_kerrokseen(self, kerros):
        if self.atm < kerros:
            Hissi.kerros_ylos(h)
        if self.atm > kerros:
            Hissi.kerros_alas(h)

    def kerros_alas(self):
        while self.atm != kerros:
            self.atm -= 1
            if self.atm == kerros:
                print(self.atm)

    def kerros_ylos(self):
        while self.atm != kerros:
            self.atm += 1
            if self.atm == kerros:
                print(self.atm)

class Talo:
    def __init__(self, alin, ylin, h_lkm):
        self.alin = alin
        self.ylin = ylin
        self.h_lkm = h_lkm
        self.hissit = []
        for i in range(1, 5):
            self.hissit.append(Hissi(1, 10, 1))

    def aja_hissia(self, h_num, kohde):


# pääohjelma

t = Talo(1, 10, 4)
h = Hissi(1, 10, 1)
kerros = int(input("Mihin kerrokseen haluat?"))
h.siirry_kerrokseen(kerros)
t.aja_hissia(kerros)