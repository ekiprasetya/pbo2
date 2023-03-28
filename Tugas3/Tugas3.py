class Hewan:
    def suara(self):
        pass

class Anjing(Hewan):
    def suara(self):
        print("Guk guk!")

class Kucing(Hewan):
    def suara(self):
        print("Meong meong!")

class Sapi(Hewan):
    def suara(self):
        print("Moo moo!")

class Ayam(Hewan):
    def suara(self):
        print("Kukuruyuk!")

class Kambing(Hewan):
    def suara(self):
        print("Mbeee mbeee!")

class Bebek(Hewan):
    def suara(self):
        print("Kwek kwek!")

class Burung(Hewan):
    def suara(self):
        print("Cuit cuit!")

class Kelinci(Hewan):
    def suara(self):
        print("Kring kring!")

class Singa(Hewan):
    def suara(self):
        print("Roaarrr!")

# Membuat objek dari masing-masing kelas hewan
hewan1 = Anjing()
hewan2 = Kucing()
hewan3 = Sapi()
hewan4 = Ayam()
hewan5 = Kambing()
hewan6 = Bebek()
hewan7 = Burung()
hewan8 = Kelinci()
hewan9 = Singa()
hewan10 = Kelinci()

# Memanggil metode suara() untuk masing-masing objek hewan
hewan1.suara() # Output: Guk guk!
hewan2.suara() # Output: Meong meong!
hewan3.suara() # Output: Moo moo!
hewan4.suara() # Output: Kukuruyuk!
hewan5.suara() # Output: Mbeee mbeee!
hewan6.suara() # Output: Kwek kwek!
hewan7.suara() # Output: Cuit cuit!
hewan8.suara() # Output: Kring kring!
hewan9.suara() # Output: Roaarrr!
hewan10.suara() # Output: Kring kring!
