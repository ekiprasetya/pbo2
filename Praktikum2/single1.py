class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "bergerak")
        
class Anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Raug!")

anjing = Anjing("Dogy", 1, "Siberian Husky")
anjing.bergerak()
anjing.bersuara()