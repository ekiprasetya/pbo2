# class induk
class Kendaraan:
    def __init__(self, nama, jumlah_roda):
        self.nama = nama
        self.jumlah_roda = jumlah_roda

    def info(self):
        print("Kendaraan:", self.nama)
        print("Jumlah roda:", self.jumlah_roda)

# class turunan 1
class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_roda, merk):
        super().__init__(nama, jumlah_roda)
        self.merk = merk

    def info(self):
        super().info()
        print("Merk:", self.merk)

# class turunan 2
class Motor(Kendaraan):
    def __init__(self, nama, jumlah_roda, merek):
        super().__init__(nama, jumlah_roda)
        self.merek = merek

    def info(self):
        super().info()
        print("Merek:", self.merek)

# membuat objek dari kelas Mobil
mobil1 = Mobil("Avanza", 4, "Toyota")
mobil1.info()

# membuat objek dari kelas Motor
motor1 = Motor("Vario", 2, "Honda")
motor1.info()
