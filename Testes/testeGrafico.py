from tkinter import *
import tkinter

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.criarEixos()
        self.root.mainloop()
    def tela(self):
        self.root.geometry("800x800")
        self.root.title("Grafico")
        self.root.config(background="red")
        self.root.resizable(False, False)
    def widgets(self):
        self.canvas = Canvas(self.root, background="black")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    def criarEixos(self):
        height = 800
        width = 800

        self.canvas.create_line(0, height / 2, width, height / 2, fill="green")
        self.canvas.create_line(width / 2, 0, width / 2, height, fill="green")
if __name__ == "__main__":
    App()