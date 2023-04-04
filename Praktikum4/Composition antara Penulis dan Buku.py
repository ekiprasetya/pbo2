class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def menulis_buku(self, judul):
        buku = Buku(judul, self)
        return buku
    
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def detail(self):
        print(f"Buku dengan judul {self.judul} ditulis oleh {self.penulis.nama}")
penulis1 = Penulis("Mary Sue")
buku1 = penulis1.menulis_buku("Pohon di Tengah Kota")
buku1.detail()