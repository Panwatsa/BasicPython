from tkinter import * #เป็นการ import ทั้งหมด
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณราคาหนังสือการ์ตูน')
GUI.geometry('700x600')



L = Label(GUI,text='กรุณากรอกจำนวณหนังสือ',font=(None,20))
L.pack()

bg = PhotoImage(file='Manga.png')

BG = Label(GUI, image=bg)
BG.pack()

v_quantity = StringVar() #ตัวแปรที่ใช้เก็บข้อความที่พิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack(pady=10)


def Cal():
    try:    
        quan = float(v_quantity.get())
        calc = quan * 70 #ราคาเล่มละ 70 บาท * จำนวนหนังสือ
        messagebox.showinfo('ราคาทั้งหมด','ราคาหนังสือทั้งหมด {} บาท'.format(calc))
        v_quantity.set(' ')
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set(' ')


B = ttk.Button(GUI, text='คำนวณ', command=Cal)
B.pack(ipadx=30,ipady=10,) #ipadx ขยายความกว้าง x,y



GUI.mainloop() #เพื่อให้โปรแกรม run ตลอดเวลา
