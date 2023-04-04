class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def tulis_buku(self, judul):
        buku = Buku(judul, self)
        return buku

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def rilis(self, tanggal):
        self.tanggal_rilis = tanggal
penulis1 = Penulis('J.K. Rowling')
buku1 = penulis1.tulis_buku('Harry Potter and the Philosopher\'s Stone')
buku1.rilis('26 June 1997')