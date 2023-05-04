# Contoh Exception Handling untuk Type Error
try:
    x = '5' + 2
except TypeError as e:
    print(f'Terdapat TypeError: {e}')

# Contoh Exception Handling untuk ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f'Terdapat ZeroDivisionError: {e}')

# Contoh Exception Handling untuk FileNotFoundError
try:
    with open('file_tidak_ada.txt') as f:
        print(f.read())
except FileNotFoundError as e:
    print(f'Terdapat FileNotFoundError: {e}')

# Contoh Exception Handling untuk KeyError
dictionary = {'a': 1, 'b': 2}
try:
    print(dictionary['c'])
except KeyError as e:
    print(f'Terdapat KeyError: {e}')

# Contoh Exception Handling untuk IndexError
list_angka = [1, 2, 3]
try:
    print(list_angka[3])
except IndexError as e:
    print(f'Terdapat IndexError: {e}')

# Contoh Exception Handling untuk AttributeError
class Contoh:
    def __init__(self, x):
        self.x = x

c = Contoh(5)
try:
    print(c.y)
except AttributeError as e:
    print(f'Terdapat AttributeError: {e}')

# Contoh Exception Handling untuk ValueError
try:
    x = int('abc')
except ValueError as e:
    print(f'Terdapat ValueError: {e}')

# Contoh Exception Handling untuk NameError
try:
    x = y + 5
except NameError as e:
    print(f'Terdapat NameError: {e}')

# Contoh Exception Handling untuk KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print('Program dihentikan oleh pengguna')

# Contoh Exception Handling untuk MemoryError
try:
    x = ' ' * 10**9
except MemoryError as e:
    print(f'Terdapat MemoryError: {e}')
