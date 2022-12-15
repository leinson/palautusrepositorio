from tekoaly import Tekoaly
from kivi_sakset_paperi import KiviSaksetPaperi

class KPSTekoaly(KiviSaksetPaperi):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()
    
    def _toisen_siirto(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
       
