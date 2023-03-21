# class induk
class Binatang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print("Binatang:", self.nama)
        print("Umur:", self.umur)

# class turunan 1
class Mamalia(Binatang):
    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def info(self):
        super().info()
        print("Jenis:", self.jenis)

# class turunan 2
class Reptil(Binatang):
    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def info(self):
        super().info()
        print("Jenis:", self.jenis)

# membuat objek dari kelas Mamalia
mamalia1 = Mamalia("Harimau", 5, "Karnivora")
mamalia1.info()

# membuat objek dari kelas Reptil
reptil1 = Reptil("Kadal", 2, "Herbivora")
reptil1.info()
