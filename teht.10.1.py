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
                print("Olet kerroksessa", (self.atm))

    def kerros_ylos(self):
        while self.atm != kerros:
            self.atm += 1
            if self.atm == kerros:
                print("Olet kerroksessa", (self.atm))

# pääohjelma

h = Hissi(1, 10, 1)
kerros = int(input("Mihin kerrokseen haluat?(1-10) "))
h.siirry_kerrokseen(kerros)