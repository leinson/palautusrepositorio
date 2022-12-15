from kivi_sakset_paperi import KiviSaksetPaperi

class KPSPelaajaVsPelaaja(KiviSaksetPaperi):
    def __init__(self) -> None:
        super().__init__()

    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")
