import tkinter
from tkinter import *
from Projetos import bhaskara
class MathFuncs():
    def bhaskara(self):
        a = 1
        b = -6
        c = 5

        delta = (b**2) - 4 * (a) * (c)
        raizDelta = delta**(1/2)

        x1 = (-(b) + raizDelta)/(2*a)
        x2 = (-(b) - raizDelta)/(2*a)

        print(f"X' = {x1}")
        print(f"X'' = {x2}")

class Application(MathFuncs):
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("500x700")
    def widgets(self):
        btn1 = Button(self.root, text="Bhaskara", command=self.bhaskara)
        btn1.place(relx=0.05, rely=0.05, relheight=0.05, relwidth=0.2)


if __name__ == "__main__":
    Application()