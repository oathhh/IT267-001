from vehicle import Vehicle

class Bus(Vehicle):
    def init(self, name, wheels, max_speed, vin) -> None:
        super().init(name, wheels, max_speed, vin)

    def set_color(self,color):
        self.set_color = color

    def set_capacity(self,capacity):
        self.set_capacity = capacity

    def bus_detail(self):
        self.v_detail
        print(f'color : {self.set_color}')
        print(f'capacity : {self.set_capacity}')