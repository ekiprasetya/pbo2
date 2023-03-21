class TemperatureConverter:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return (self.celcius * 9/5) + 32

    def to_reamur(self):
        return self.celcius * 4/5

    def to_kelvin(self):
        return self.celcius + 273.15

# contoh penggunaan
temperature = TemperatureConverter(25)

print(f"{temperature.celcius} C = {temperature.to_fahrenheit()} F")
print(f"{temperature.celcius} C = {temperature.to_reamur()} R")
print(f"{temperature.celcius} C = {temperature.to_kelvin()} K")
