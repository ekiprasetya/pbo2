class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.kelompok_kkm = None

    def join_kelompok_kkm(self, kelompok_kkm):
        self.kelompok_kkm = kelompok_kkm

    def lihat_kelompok_kkm(self):
        return self.kelompok_kkm

class KelompokKKM:
    def __init__(self, nomor):
        self.nomor = nomor
        self.anggota = []

    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)

    def lihat_anggota(self):
        return self.anggota

# Membuat objek mahasiswa dan kelompok KKM
mahasiswa1 = Mahasiswa("Bob")
kelompok1 = KelompokKKM(1)

# Mahasiswa bergabung dengan kelompok KKM
mahasiswa1.join_kelompok_kkm(kelompok1)
kelompok1.tambah_anggota(mahasiswa1)

# Melihat kelompok KKM dari mahasiswa
print(mahasiswa1.lihat_kelompok_kkm().nomor)

# Melihat anggota dari kelompok KKM
for anggota in kelompok1.lihat_anggota():
    print(anggota.nama)
