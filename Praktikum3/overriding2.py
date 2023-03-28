class BangunDatar:
    def __init__(self, panjang=None, lebar=None, jari=None):
        if panjang is not None and lebar is not None:
            self.panjang = panjang
            self.lebar = lebar
        elif jari is not None:
            self.jari = jari

    def hitungLuas(self):
        pass

class PersegiPanjang(BangunDatar):
    def hitungLuas(self):
        return self.panjang * self.lebar

class Lingkaran(BangunDatar):
    def hitungLuas(self):
        return 3.14 * self.jari * self.jari

# Membuat objek dari kelas PersegiPan
