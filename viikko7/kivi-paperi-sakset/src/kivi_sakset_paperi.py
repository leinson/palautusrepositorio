from tuomari import Tuomari

class KiviSaksetPaperi:
    def pelaa(self):
        tuomari = Tuomari()
        ekan_siirto = self._ensimmasen_siirto()
        tokan_siirto = self._toisen_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmasen_siirto()
            tokan_siirto = self._toisen_siirto()

        print("Kiitos!")
        print(tuomari)

    def _ensimmasen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

