class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
class Pengarang:
    def __init__(self, karangan, genre):
        self.karangan = karangan
        self.genre = genre
    def display_info(self):
        print(f"Buku: {self.karangan}")
        print(f"Genre: {self.genre}")
class PengarangPekerja(Orang, Pekerja, Pengarang):
    def __init__(self, nama, umur, pekerjaan, gaji, karangan, genre):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Pengarang.__init__(self, karangan, genre)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Karangan: {self.karangan}")
        print(f"Genre: {self.genre}")
# contoh penggunaan
pengarang_pekerja = PengarangPekerja("John Deep", 25, "Pengarang", "$5000", "The World", "Fantasy")
pengarang_pekerja.display_info()