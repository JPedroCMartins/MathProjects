from tkinter import *
import tkinter

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.criarEixos()
        self.bhaskara(1,2,-3)
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
        self.canvas.create_oval(self.center_x - self.ponto, self.center_y - self.ponto, self.center_x + self.ponto, self.center_y + self.ponto, fill="green")
    def MarcarCoordenada(self, x, y):
        coord_x = self.center_x + x * (self.width / 20)
        coord_y = self.center_y - y * (self.height / 20)

        self.canvas.create_oval(coord_x - self.ponto, coord_y - self.ponto,
                                coord_x + self.ponto, coord_y + self.ponto, fill="red")

        return coord_y, coord_x

    def bhaskara(self, a, b, c):
        list_x = []
        list_y = []

        list_y_2 = []
        list_x_2 = []
        for x in range(7):
            x = -x
            y = (a*x**2) + (b*x) + (c)
            self.MarcarCoordenada(x, y)
            list_y.append(y)
            list_x.append(x)

        for x in range(6):
            y = (a * x ** 2) + (b * x) + (c)
            self.MarcarCoordenada(x, y)
            list_y_2.append(y)
            list_x_2.append(x)



        for i in range(len(list_x) - 1):
            x1, y1 = list_x[i], list_y[i]
            x2, y2 = list_x[i + 1], list_y[i + 1]
            y1, x1 = self.MarcarCoordenada(x1, y1)  # Marcar ponto de início da linha
            y2, x2 = self.MarcarCoordenada(x2, y2)  # Marcar ponto de fim da linha
            self.canvas.create_line(x1, y1, x2, y2, fill="blue")

        for i in range(len(list_x_2) - 1):
            x1, y1 = list_x_2[i], list_y_2[i]
            x2, y2 = list_x_2[i + 1], list_y_2[i + 1]
            y1, x1 = self.MarcarCoordenada(x1, y1)  # Marcar ponto de início da linha
            y2, x2 = self.MarcarCoordenada(x2, y2)  # Marcar ponto de fim da linha
            self.canvas.create_line(x1, y1, x2, y2, fill="blue")


if __name__ == "__main__":
    App()