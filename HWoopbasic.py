
from turtle import st
from unicodedata import name

class Manga:
    def __init__(self,name,genres,price):
        self.name = name
        self.genres = genres
        self.price = price
    
    def myreading(self):
        print(f'ฉันกำลังอ่าน{self.name} ราคา{self.price} บาท')

    def myprice(self):
        if self.price >= 100:
            print('หนังสือเล่มนี้ราคาแพง')
        else:
            print('หนังสือเล่มนี้ราคาถูก')

if __name__ == '__main__':
    manga1 = Manga('Ganz','Action',125)
    manga2 = Manga('Who_made_me_the_princess','Romance',200)
    manga3 = Manga('Reborn','Action',50)


    print('---10.00 น.---')
    manga1.myreading()
    manga1.myprice()
    print('---12.00 น.---')
    manga2.myreading()
    manga2.myprice()
    print('---00.00 น.---')
    manga3.myreading()
    manga3.myprice()