class Hissi:
    def __init__(self, alin, ylin, atm):
        self.alin = alin
        self.ylin = ylin
        self.atm = atm

    def siirry_kerrokseen(self, kohde):
        if self.atm < kohde:
            Hissi.kerros_ylos(h)
        if self.atm > kohde:
            Hissi.kerros_alas(h)

    def kerros_alas(self):
        while self.atm != kohde:
            self.atm -= 1
            if self.atm == kohde:
                print("Olet kerroksessa", (self.atm))

    def kerros_ylos(self):
        while self.atm != kohde:
            self.atm += 1
            if self.atm == kohde:
                print("Olet kerroksessa", (self.atm))

class Talo:
    def __init__(self, alin, ylin, h_lkm):
        self.alin = alin
        self.ylin = ylin
        self.h_lkm = h_lkm
        self.hissit = []
        for i in range(1, 5):
            self.hissit.append(Hissi(1, 10, 1))

    def aja_hissia(self, h_num, kohde):
        elevator = self.hissit[h_num - 1]
        print(f"Ajetaan hissiä {h_num}")
        elevator.siirry_kerrokseen(kohde)

    def palohälytys(self):
        for h in self.hissit:
            h.siirry_kerrokseen(self.alin)


# pääohjelma

t = Talo(1, 10, 4)
h = Hissi(1, 10, 1)
hissi = int(input("Valitse hissi:(1-4) "))
kohde = int(input("Mihin kerrokseen haluat?(1-10) "))
t.aja_hissia(hissi, kohde)