from turtle import st
from unicodedata import name


class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(f'{self.name}กำลังเรียน...')

    def sawatdee(self):
        if self.gender == 'ชาย':
            tail = 'ครับ'
            callme = 'ผม'
        else:
            tail = 'ค่ะ'
            callme = 'หนู'
        print(f'สวัสดี{tail} {callme}ชื่อ{self.name}') #เป็นการเติมหางเสียง

class SpecialStudent(Student): #เป็นการสือบทอดคลาสมาจากอันก่อนหน้า

    def __inite__(self,name,age,gender,parent):
        super().__init__(name,age,gender) #เป็นการเรียกตัวแปร Student
        self.parent = parent
    
    def hello(self, person='เพื่อน'):
            if person == 'เพื่อน':
                print('เอาการบ้านมาลอกดิ้!')
            else:
                print('ได้เลย')
    

class Teacher:
    def __init__(self,name,gender,subject):
        self.name = name
        self.gender = gender
        self.subject = subject

    def teach(self):
        print('คุณครู{}กำลังสอนวิชา{}'.format(self.name,self.subject))


if __name__ == '__main__':
    student1 = Student('สมเกียรติ',16,'ชาย')
    student2 = Student('สมใจ',14,'หญิง')
    teacher1 = Teacher('สมศรี','หญิง','คณิตศาสตร์')
    speacial_student = SpecialStudent('หมู',15,'ชาย',)
    
    #print(teacher1.name)
    #print(teacher1.subject)

    print('----- 10.30 น. ------')
    student1.sawatdee()
    student2.sawatdee()
    teacher1.teach()
    student1.study()
    student2.study()
    print('----- 12.30 น. ------')
    speacial_student.hello()
