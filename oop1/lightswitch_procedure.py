#สร้างฟังค์ช้นเปิด ปิดไฟ
global switch_status

#สร้างฟังค์ชันเปิดไฟ
def turnon():
    global switch_status
    switch_stasus = True

#สร้างฟังค์ชันปิดไฟ
def turnoff():
    global switch_status
    switch_stasus = False

switch_stasus = False

print(f"status = {switch_stasus}")
turnon()
print(f"status = {switch_stasus}")
turnoff()
print(f"status = {switch_stasus}")

print(f"status = {switch_stasus}")
