# class induk
class Kendaraan:
    def __init__(self, nama, jumlah_roda):
        self.nama = nama
        self.jumlah_roda = jumlah_roda

    def info(self):
        print("Kendaraan:", self.nama)
        print("Jumlah roda:", self.jumlah_roda)

# class turunan level 1
class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_roda, merk):
        super().__init__(nama, jumlah_roda)
        self.merk = merk

    def info(self):
        super().info()
        print("Merk:", self.merk)

# class turunan level 2
class Sedan(Mobil):
    def __init__(self, nama, jumlah_roda, merk, kapasitas_mesin):
        super().__init__(nama, jumlah_roda, merk)
        self.kapasitas_mesin = kapasitas_mesin

    def info(self):
        super().info()
        print("Kapasitas mesin:", self.kapasitas_mesin)

# membuat objek dari kelas Sedan
sedan1 = Sedan("Avanza", 4, "Toyota", "1500 cc")
sedan1.info()