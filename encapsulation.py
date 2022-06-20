from unicodedata import name


class BangAccount:
    def __init__(self, name, age, amount):
        self.name = name
        self._age = age #protected
        self.__amount = amount #private

    def showMessage(self):
        print('กำลังทำรายการฝาก-ถอนในบัญชี')

    def _deposit(self, deposit):
        self.__amount += deposit
        print(f'ฝากเพิ่ม {deposit} รวมเงิน {self.__amount}')

    @property
    def amounts(self): #Getter
        return self.__amount
    
    @amounts.setter
    def amounts(self, amount): #Setter
        self.__amount = amount

    def __withdraw(self, withdraw):
        self.__amount -= withdraw
        print(f'ถอนออก {withdraw} เหลือเงิน {self.__amount}')

    

class Employee(BangAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)

if __name__ == '__main__':
    employee = Employee('กริดคุง', 70, 20000)
    print(employee.name)
    print(employee._age)
    print(employee.amounts)

    employee.amounts = 10000
    print(employee.amounts)

    #employee.data = 10000
    #employee.showMessage()
    #employee._deposit(5000)
    