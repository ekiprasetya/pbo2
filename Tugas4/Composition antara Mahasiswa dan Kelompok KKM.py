class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.kelompok = None
    
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok

class KelompokKKM:
    def __init__(self, nomor, anggota=[]):
        self.nomor = nomor
        self.anggota = anggota
    
    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)
    
    def hapus_anggota(self, mahasiswa):
        self.anggota.remove(mahasiswa)
mhs1 = Mahasiswa('Jane Doe', '1234567890')
mhs2 = Mahasiswa('Alice Smith', '0987654321')
kelompok1 = KelompokKKM('1')
kelompok1.tambah_anggota(mhs1)
kelompok1.tambah_anggota(mhs2)