import random


class Auto:
    def init(self, rekkari, huippu):
        self.rekkari = rekkari
        self.huippu = huippu
        self.atm = 0
        self.matka = 0
        self.aika = 0

    def kiihdytys(self, nopeus):
        self.atm = self.atm + nopeus
        if self.atm > self.huippu:
            self.atm = self.huippu
        elif self.atm < 0:
            self.atm = 0

    def kuljettu_matka(self, tunnit):
        self.matka += (self.atm * tunnit)

    def tulostaAuto(self):
        print(self.rekkari, self.atm, self.matka)


class Kilpailu:

    def init(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytys(random.randint(-10, 15))
            auto.kuljettu_matka(1)

    def tulosta_tilanne(self):
        for auto in autot:
            auto.tulostaAuto()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
            else:
                continue


def autojen_luonti():
    autot = []
    for i in range(10):
        autot.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))
    return autot


autot = autojen_luonti()
tunti = 0
romuralli = Kilpailu("Suuri romuralli", 8000, autot)
while True:
    romuralli.tunti_kuluu()

    if romuralli.kilpailu_ohi():
        print("Kilpailu ohi!\n")
        romuralli.tulosta_tilanne()
        break

    else:
        tunti += 1

        if tunti % 10 == 0:
            print(f"Tunti: {tunti}\n")
            romuralli.tulosta_tilanne()

        else:
            continue