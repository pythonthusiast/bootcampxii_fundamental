tujuan = 'Mempelajari modularisasi di Python'
print(tujuan)

# TANPA MODULARISASI
alas = 6
tinggi = 4
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

alas = 16
tinggi = 4
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)


# MODULARISASI DENGAN FUNCTION
def hitung_luas_segitiga(alas, tinggi):
    print('fungsi', alas)
    return alas * tinggi / 2


print(hitung_luas_segitiga(6, 7))

# TUGAS BUAT FUNGSI MENGHITUNG BUJUR SANGKAR = sisi * sisi

# MODULARISASI DENGAN CLASS YANG DISEBUT DENGAN OBJECT ORIENTED PROGRAMMING (OOP)
# CLASS = GABUNGAN ANTARA VARIABEL DAN FUNGSI KE DALAM SATU TEMPAT

# TIGA KONSEP OOP
# ENCAPSULATION = MEMBUAT KELAS
# INHERITANCE = MEMBUAT KELAS DARI KELAS YANG SUDAH ADA
# POLYMORPHISM = METHOD PADA KELAS DIBAWAHNYA, BERPERILAKU BERBEDA-BEDA


class Geometry:
    def get_stats(self):
        pass

    def print_stats(self):
        print('Statistik bangun ini', self.get_stats())


class SegiTiga(Geometry):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

    def get_stats(self):
        # return 'Alas = {}, Tinggi = {}, Luas = {}'.format(self.alas, self.tinggi, self.hitung_luas())
        return f'Alas = {self.alas}, Tinggi = {self.tinggi}, Luas = {self.hitung_luas()}'



s1 = SegiTiga(5, 8)
s2 = SegiTiga(4, 9)

print('S1 alas', s1.alas)
print('S2 alas', s2.alas)
s1.print_stats()

print(f'S1 luas {s1.hitung_luas()}')

# TUGAS BUAT CLASS BUJURSANGKAR
# RAMPUNGKAN BUJURSANGKAR SEBAGAI ANAK GEOMETRY
