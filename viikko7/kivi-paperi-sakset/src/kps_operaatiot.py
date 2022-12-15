from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

class KpsOperaatiot:
    @staticmethod
    def luo(operaatio):
        if operaatio == "kaksinpeli":
            kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.pelaa()

        elif operaatio == "yksinpeli":
            yksinpeli = KPSTekoaly()
            yksinpeli.pelaa()

        elif operaatio == "haastava_yksinpeli":
            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()