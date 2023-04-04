class Peneliti:
    def __init__(self, nama):
        self.nama = nama
        self.jurnal = None

    def submit_jurnal(self, jurnal):
        self.jurnal = jurnal

    def lihat_jurnal(self):
        return self.jurnal

class Jurnal:
    def __init__(self, judul):
        self.judul = judul
        self.penulis = None

    def tulis_jurnal(self, penulis):
        self.penulis = penulis

    def lihat_penulis(self):
        return self.penulis

# Membuat objek peneliti dan jurnal
peneliti1 = Peneliti("Alice")
jurnal1 = Jurnal("Judul Jurnal 1")

# Peneliti menulis jurnal
jurnal1.tulis_jurnal(peneliti1)
peneliti1.submit_jurnal(jurnal1)

# Peneliti melihat jurnal yang telah ditulisnya
print(peneliti1.lihat_jurnal())

# Melihat penulis dari jurnal
print(jurnal1.lihat_penulis().nama)
