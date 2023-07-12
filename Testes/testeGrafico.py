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
        self.height = 800
        self.width = 800

        self.center_x = self.width / 2
        self.center_y = self.height /2
        self.ponto = 5

        self.canvas.create_line(0, self.height / 2, self.width, self.height / 2, fill="green")
        self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, fill="green")

        self.canvas.create_oval(self.center_x - self.ponto, self.center_y - self.ponto,
                                self.center_x + self.ponto, self.center_y + self.ponto, fill="red")
    def MarcarCoordenada(self, x, y):
        coord_x = self.center_x + x * (self.width / 20)
        coord_y = self.center_y - y * (self.height / 20)

        self.canvas.create_oval(coord_x - self.ponto, coord_y - self.ponto,
                                coord_x + self.ponto, coord_y + self.ponto, fill="red")
if __name__ == "__main__":
    App()