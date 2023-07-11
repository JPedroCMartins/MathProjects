import tkinter
from tkinter import *

class Application():
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("500x700")
    def widgets(self):
        btn1 = Button(self.root, text="teste", command=self.hello)
        btn1.place(relx= 0.2, rely = 0.05, relheight=0.05, relwidth=0.2)
    def hello(self):
        print("Hello")

if __name__ == "__main__":
    Application()