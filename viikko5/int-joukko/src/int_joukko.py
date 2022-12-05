KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti: int=KAPASITEETTI, kasvatuskoko: int=OLETUSKASVATUS):
        self.kasvatuskoko = kasvatuskoko
        self.kapasiteetti = kapasiteetti
        self.tarkista_kapasiteetti(self.kapasiteetti, self.kasvatuskoko)
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def tarkista_kapasiteetti(self, kapasiteetti, kasvatuskoko):
        if kapasiteetti < 1 or kasvatuskoko < 0:
            raise ValueError("Kapasiteetti ja kasvatuskoko täytyy olla positiivisia lukuja.")

    def kuuluu_lukujonoon(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True
        return False

    def uusi_luku(self, n):
        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        if self.alkioiden_lkm % len(self.lukujono) == 0:
            lukujono_kopio = self.lukujono
            self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(lukujono_kopio, self.lukujono)
    
    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm += 1
            return True
        if not self.kuuluu_lukujonoon(n):
            self.uusi_luku(n)
            return True
        return False

    def poista(self, n):
        poistettava = -1
        apu = 0
        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                poistettava = i
                break
        if poistettava != -1:    
            for j in range(poistettava, self.alkioiden_lkm - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu
            self.alkioiden_lkm -= 1
            return True
        return False

    def alkioiden_lukumaara(self):
        return self.alkioiden_lkm

    def lukulistaksi(self):
        luku_lista = [0] * self.alkioiden_lkm
        for i in range(len(luku_lista)):
            luku_lista[i] = self.lukujono[i]
        return luku_lista

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.lukulistaksi()
        b_taulu = b.lukulistaksi()
        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])
        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.lukulistaksi()
        b_taulu = b.lukulistaksi()
        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.lukulistaksi()
        b_taulu = b.lukulistaksi()
        for i in range(len(a_taulu)):
            z.lisaa(a_taulu[i])
        for i in range(len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = "{" + str(self.lukujono[i])+", "
            tuotos += str(self.lukujono[self.alkioiden_lkm - 1])+"}"
            return tuotos
