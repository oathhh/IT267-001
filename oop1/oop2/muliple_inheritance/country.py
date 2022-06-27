from geograrphic import Geographic
from temperature import Temperature


class Conutry (Geographic, Temperature):
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population

    def getPopurationDenaity(self):
        return self.population / self.area

    def showDetails(self):
        print(f'country: {self.name}')
        print(f'Area: {self.area:,.2f}')
        print(f'Population: {self.population:,}')
        print(f'Density: {self.getPopurationDenaity():,.2f}')
        print(f'Decimal cordinate: {self.getcordinate() }')
        print(f'Time zone: {self.gettimezone() }')
        print(f'Climate {self.getclimate() }')
        print(f'Temperature in Celsius: {self.celsius}')
        print(f'Temperature in Fahrenheit: {self.getFahrenheit():.2f}')
        print(f'The weather in {self.getWeather()}')
        
        print('***********************************')