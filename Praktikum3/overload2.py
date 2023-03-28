class BangunDatar:
    def __init__(self, panjang=None, lebar=None, jari=None):
        if panjang is not None and lebar is not None:
            self.panjang = panjang
            self.lebar = lebar
        elif jari is not None:
            self.jari = jari

class PersegiPanjang(BangunDatar):
    def hitungLuas(self):
        return self.panjang * self.lebar

class Lingkaran(BangunDatar):
    def hitungLuas(self):
        return 3.14 * self.jari * self.jari

# Membuat objek dari kelas PersegiPanjang
p = PersegiPanjang(4, 5)

# Memanggil metode hitungLuas untuk objek p
print(p.hitungLuas()) # Output: 20

# Membuat objek dari kelas Lingkaran
l = Lingkaran(jari=7)

# Memanggil metode hitungLuas untuk objek l
print(l.hitungLuas()) # Output: 153.86
