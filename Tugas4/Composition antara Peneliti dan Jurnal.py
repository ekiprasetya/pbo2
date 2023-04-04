class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_artikel(self, judul):
        artikel = Artikel(judul, self)
        return artikel

class Jurnal:
    def __init__(self, nama, issn):
        self.nama = nama
        self.issn = issn
        self.artikels = []
    
    def tambah_artikel(self, artikel):
        self.artikels.append(artikel)

class Artikel:
    def __init__(self, judul, peneliti):
        self.judul = judul
        self.peneliti = peneliti
        self.jurnal = None
    
    def terbit_di(self, jurnal):
        self.jurnal = jurnal
        jurnal.tambah_artikel(self)
peneliti1 = Peneliti('John Doe', 'Fisika')
jurnal1 = Jurnal('Journal of Physics', '1234-5678')
artikel1 = peneliti1.tulis_artikel('The Theory of Everything')
artikel1.terbit_di(jurnal1)