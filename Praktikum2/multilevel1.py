# class induk
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print("Hewan:", self.nama)
        print("Umur:", self.umur)

# class turunan level 1
class Mamalia(Hewan):
    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def info(self):
        super().info()
        print("Jenis:", self.jenis)

# class turunan level 2
class Gajah(Mamalia):
    def __init__(self, nama, umur, jenis, berat):
        super().__init__(nama, umur, jenis)
        self.berat = berat

    def info(self):
        super().info()
        print("Berat:", self.berat)

# membuat objek dari kelas Gajah
gajah1 = Gajah("Gajah Sumatera", 10, "Herbivora", 2000)
gajah1.info()
