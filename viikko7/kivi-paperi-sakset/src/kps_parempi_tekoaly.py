from tekoaly_parannettu import TekoalyParannettu
from kivi_sakset_paperi import KiviSaksetPaperi

class KPSParempiTekoaly(KiviSaksetPaperi):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(tokan_siirto)
        return tokan_siirto