from bangunruang.geometry import Geometry


class SegiTiga(Geometry):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

    def get_stats(self):
        # return 'Alas = {}, Tinggi = {}, Luas = {}'.format(self.alas, self.tinggi, self.hitung_luas())
        return f'Alas = {self.alas}, Tinggi = {self.tinggi}, Luas = {self.hitung_luas()}'