

class Car:
    brand = None
    year = None
    fuel = None
    status = None

    def __init__(self,brand,year,fuel,status):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = status

    def checkStatus(self):
        if self.status == True:
            print('รถยนต์คันนี้ผ่านการทดสอบแล้ว')
        else:
            print('รถยนต์คันนี้ยังไม่ผ่านการทดสอบ')

       
       

    def drive(self):
        print('รถยนต์คันนี้กำลังขับเคลื่อน')

if __name__ == '__main__': #คำสั่งมาจากคลาสที่อยู่ในไฟล์หรือโมดูลเดียวกันหรือไม่
    car1 = Car('Benz', 2010, 20, True)
    car2 = Car('BMW', 2020, 50, False)
    
    
    
    #print(type(car1)) #เป็นชนิด object ที่อยู่ใน class car
    #print(type(car2))
    print(f'ยี่ห้อ : {car1.brand}')
    print(f'ปีที่ผลิต : {car1.year}')
    print(f'ระดับเชื้อเพลิง : {car1.fuel}')

    car1.checkStatus()
    car1.drive()
    
    print('-----------------')
    
    print(f'ยี่ห้อ : {car2.brand}')
    print(f'ปีที่ผลิต : {car2.year}')
    print(f'ระดับเชื้อเพลิง : {car2.fuel}')

    car2.checkStatus()
    car2.drive()
