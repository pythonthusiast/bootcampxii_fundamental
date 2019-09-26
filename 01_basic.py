# Program penghitung luas segitiga
#SEQUENTIAL
nama = 'Eko'
alas = 6
tinggi = 4
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

# ERROR, karena alas sudah menjadi string = text
# alas = 'enam'
# luas_segitiga = alas * tinggi / 2
# print(luas_segitiga)

#BRANCHING
print('Program oleh', nama)
if luas_segitiga >= 100:
    print('Segitiga yang besar!')
    print('------')
else:
    print('Kecil')
    print('------')

#LOOP
for i in range(0, int(luas_segitiga)):
    print('Luas ke', i)

#TIPE DATA MAJEMUK
#LIST / ARRAY
daftar_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
print(daftar_hari[0])
print(len(daftar_hari))

print('Cetak list dengan for')
for hari in daftar_hari:
    print(hari)

#DICTIONARY
# KVP
# Key Value Pairs
days = {}
days['Senin'] = 'Monday'
days['Selasa'] = 'Tuesday'
days['Rabu'] = 'Wednesday'
days['Kamis'] = 'Thursday'
days['Jumat'] = 'Friday'
days['Sabtu'] = 'Saturday'
days['Minggu'] = 'Sunday'

print('Cek kamus!')
print(days['Jumat'])

# JSON = DICTIONARY di PYTHON
profil = {
    'nama': 'Eko',
    'alamat': 'Glagah',
    'pendidikan': {
        'sd': 'sd 5',
        'smp': 'smp 5',
        'sma': 'sma 3',
    }
}

print(profil['pendidikan']['sd'])
# TUGAS BUAT INFORMASI LENGKAP SD : NAMA, ALAMAT