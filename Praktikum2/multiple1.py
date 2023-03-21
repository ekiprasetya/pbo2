class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis
    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")
class Reptile(Hewan):
    def __init__(self, nama):
        self.nama = nama
    def display_info(self):
        super().display_info()
        print(f"Nama Reptile: {self.nama}")
class Karnivora(Hewan):
    def __init__(self, jenis, makanan):
        super().__init__(jenis)
        self.makanan = makanan
    def display_info(self):
        super().display_info()
        print(f"Jenis makanan: {self.makanan}")
class Buaya(Reptile, Karnivora):
    def __init__(self, jenis, nama, makanan):
        Reptile.__init__(self, nama)
        Karnivora.__init__(self, jenis, makanan)
    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")

buaya = Buaya("Reptile", "Buaya air tawar", "Daging")
buaya.display_info()