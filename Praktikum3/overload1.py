class Bilangan:
    def tambah(self, a, b):
        return a + b

    def tambah(self, a, b):
        return float(a) + float(b)

# Membuat objek dari kelas Bilangan
b = Bilangan()

# Memanggil metode tambah dengan parameter bilangan bulat
print(b.tambah(2, 3)) # Output: 5

# Memanggil metode tambah dengan parameter bilangan pecahan
print(b.tambah(2.5, 3.7)) # Output: 6.2
