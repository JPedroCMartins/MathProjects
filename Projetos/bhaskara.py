import tkinter
from tkinter import *

from Style import fontes
class AppBhaskara():
    def __init__(self):
        self.root = tkinter.Tk()
        self.fonte_padrao = fontes.fonte_verdana_bhaskara_label
        self.tela()
        self.frame_graph()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("800x800")
        pass
    def frame_graph(self):
        self.frm = Frame(self.root, bg="red")
        self.frm.place(relx=0.6, rely=0.05, relwidth=0.30, relheight=0.30)

    def update_canvas(self, event):
        self.canvas.delete("all")

        width = event.width
        height = event.height

        # Desenhar o eixo x
        self.canvas.create_line(0, height / 2, width, height / 2, fill="red")

        # Desenhar o eixo y
        self.canvas.create_line(width / 2, 0, width / 2, height, fill="green")

        # Marcar o ponto de encontro dos eixos
        self.canvas.create_oval(width / 2 - 3, height / 2 - 3, width / 2 + 3, height / 2 + 3, fill="blue")

    def widgets(self):
        self.Label_a = Label(self.root, text="a:", font=self.fonte_padrao)
        self.Label_a.place(relx=0.05, rely=0.05)

        self.Label_b = Label(self.root, text="b:", font=self.fonte_padrao)
        self.Label_b.place(relx=0.05, rely=0.15)

        self.Label_c = Label(self.root, text="c:", font=self.fonte_padrao)
        self.Label_c.place(relx=0.05, rely=0.25)

        self.Entry_a = Entry(self.root, font=self.fonte_padrao)
        self.Entry_a.place(relx=0.2, rely=0.05, relheight=0.1, relwidth=0.3)

        self.Entry_b = Entry(self.root, font=self.fonte_padrao)
        self.Entry_b.place(relx=0.2, rely=0.15, relheight=0.1, relwidth=0.3)

        self.Entry_c = Entry(self.root, font=self.fonte_padrao)
        self.Entry_c.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.3)

        self.btnCalcular = Button(text="Calcular", command=self.bhaskara_calc)
        self.btnCalcular.place(relx = 0.2, rely=0.40, relheight=0.1, relwidth=0.3)

        self.lbl_resultado = Label(self.root, text="f(x) = ax^2+bx+c",font=self.fonte_padrao)
        self.lbl_resultado.place(relx=0.2, rely=0.55)

        self.canvas = tkinter.Canvas(self.frm, bg="yellow")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.canvas.bind("<Configure>", self.update_canvas)
    def bhaskara_calc(self):
        a = int(self.Entry_a.get())
        b = int(self.Entry_b.get())
        c = int(self.Entry_c.get())
        delta = (b**2) - 4 * (a) * (c)
        if delta < 0:
            print("Delta não possui valor real pois seu delta é menor que 0")
        else:
            #f(x) = ax^2 + bx + c
            raizQ_delta = delta**(1/2)
            x1 = (-(b)+raizQ_delta) / (2*a)
            x2 = (-(b)-raizQ_delta) / (2*a)

            y1 = a*x1 + b*x1 + c*x1
            y2 = a*x2 + b*x2 + c*x2
            self.lbl_resultado["text"] = f"f(x) = {a}x^2+{b}x + {c}\n\nX' = {x1}\nX'' = {x2} "
            print(x1, x2)
            print(y1, y2)

if __name__ == "__main__":
    AppBhaskara()
