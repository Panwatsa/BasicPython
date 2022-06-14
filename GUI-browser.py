# GUI-webbrowser.py

from tkinter import * # Lib: Tk interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Browser')
GUI.geometry('500x300')

def Youtube():
    webbrowser.open('https://www.youtube.com')

B1 = ttk.Button(GUI,text='Youtube',command=Youtube)
B1.pack(ipadx=20, ipady=10, pady=10)

def Facebook():
    webbrowser.open('https://www.facebook.com')

B2 = ttk.Button(GUI,text='Facebook',command=Facebook)
B2.pack(ipadx=20,ipady=10,pady=10)

def Google():
    webbrowser.open('https://www.google.com')

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20, ipady=10, pady=10)

GUI.mainloop()