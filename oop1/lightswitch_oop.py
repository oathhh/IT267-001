#lightswitch_opp.py
from typing_extensions import Self


class LightSwitch():
    def __init__(self) -> None:
        self.switch_status = False

    def turnon(self):
        Self.switch_status = True
    def turnoff(self):
        self.switch_status = False

    def show(self):
        print(f"status = {self.switch_status}")

#สร้างวัสถุ (obj) จากแม่พิมพ์ (class)
switch_obj = LightSwitch()

#เรียกใช้เมธอด/ฟังชัน
switch_obj.show() #false
switch_obj.turnon()
switch_obj.show() #True
switch_obj.turnoff()
switch_obj.show() #false
switch_obj.turnoff()
switch_obj.show() #flase
