class TemperatureConverter:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return (self.celcius * 9/5) + 32

    def to_reamur(self):
        return self.celcius * 4/5

    def to_kelvin(self):
        return self.celcius + 273.15

# subclass untuk suhu tubuh
class BodyTemperatureConverter(TemperatureConverter):
    def __init__(self, celcius):
        super().__init__(celcius)
        self.unit = "C"

    def to_fahrenheit(self):
        return super().to_fahrenheit() + 32

    def to_reamur(self):
        return super().to_reamur() * 0.8

    def to_kelvin(self):
        return super().to_kelvin() + 273.15

# contoh penggunaan
normal_temperature = TemperatureConverter(25)
body_temperature = BodyTemperatureConverter(37)

print(f"{normal_temperature.celcius} C = {normal_temperature.to_fahrenheit()} F")
print(f"{normal_temperature.celcius} C = {normal_temperature.to_reamur()} R")
print(f"{normal_temperature.celcius} C = {normal_temperature.to_kelvin()} K")

print(f"{body_temperature.celcius} C ({body_temperature.unit}) = {body_temperature.to_fahrenheit()} F")
print(f"{body_temperature.celcius} C ({body_temperature.unit}) = {body_temperature.to_reamur()} R")
print(f"{body_temperature.celcius} C ({body_temperature.unit}) = {body_temperature.to_kelvin()} K")
