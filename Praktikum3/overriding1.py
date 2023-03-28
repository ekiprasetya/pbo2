class Hewan:
    def berbicara(self):
        pass

class Anjing(Hewan):
    def berbicara(self):
        return "Guk guk!"

class Kucing(Hewan):
    def berbicara(self):
        return "Meong meong!"

# Membuat objek dari kelas Anjing
a = Anjing()

# Memanggil metode berbicara untuk objek a
print(a.berbicara()) # Output: Guk guk!

# Membuat objek dari kelas Kucing
k = Kucing()

# Memanggil metode berbicara untuk objek k
print(k.berbicara()) # Output: Meong meong!
