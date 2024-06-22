import pyautogui
import time
from tkinter import *

def ButtonCommand():
    time.sleep (5)
    mouse_coordinate = (pyautogui.position())
    Label(pencere, text=mouse_coordinate, font="Times 12 bold").pack()

#Kütüphaneyi kullanmak için "Tk" fonksiyonunu bir değere atmalısın.
pencere = Tk()
#Başlık.
pencere.title("Get Mouse Coordinate | MrMdd")
#Pencerenin boyutu
pencere.geometry("800x400")
#Label
Label(pencere, text="The value will be displayed 5 seconds after clicking the button. (x, y)", font="Times 12").pack(pady="60")
#Bir buton oluştur.
btn = Button(pencere,
                text="Get", font="Times 12 bold",
                pady="20",
                padx="80",
                cursor="hand2",
                command=ButtonCommand).pack(pady="40")

#Mutlaka kullanılmalı.
pencere.mainloop()