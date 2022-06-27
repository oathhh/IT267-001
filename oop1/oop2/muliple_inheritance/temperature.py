class Temperature:
    def setCelsius(self, celsius):
            self.celsius = celsius

    def getFahrenheit(self):
        return self.celsius * 1.8 + 32

    def getWeather(self):
        if self.celsius <= 0:
            return 'freezing'
        elif self.celsius <= 18:
            return 'cold'
        elif self.celsius <= 28:
            return 'wram'
        else:
            return 'hot'