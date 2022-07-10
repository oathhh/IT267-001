from unicodedata import name


class Vehicle:

    def __init__(self, name, wheels, max_speed, vin) -> None:
        self.name = name
        self._wheels = wheels
        self._max_speed = max_speed
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print(f'===============')
        print(f'name : {self.name}')
        print(f'wheels : {self._wheels}')
        print(f'max_speed: {self._max_speed}')
        print(f'vin: {self.__vin}')