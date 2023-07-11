import tkinter
from tkinter import *
from Projetos import bhaskara
from Style import colors
from Style import fontes
class Application():
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("500x700")
        self.root.config(background=colors.background1)
    def widgets(self):
        btn1 = Button(self.root, text="Bhaskara", command=bhaskara.AppBhaskara, font=fontes.fonte_btn_main)
        btn1.place(relx=0.05, rely=0.05, relheight=0.05, relwidth=0.2)


if __name__ == "__main__":
    Application()