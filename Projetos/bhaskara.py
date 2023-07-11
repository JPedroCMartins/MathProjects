import tkinter
from tkinter import *
import numpy as np
from Style import fontes
from Style import colors
class AppBhaskara():
    def __init__(self):
        self.root_bhaskara = tkinter.Tk()
        self.fonte_padrao = fontes.fonte_verdana_bhaskara_label
        self.tela()
        self.frame_graph()
        self.widgets()
        self.root_bhaskara.mainloop()

    def tela(self):
        self.root_bhaskara.title("Bhaskara")
        self.root_bhaskara.geometry("800x800")
        self.root_bhaskara.config(bg=colors.background1)
        pass
    def frame_graph(self):
        self.frm = Frame(self.root_bhaskara, bg="black")
        self.frm.place(relx=0.6, rely=0.05, relwidth=0.30, relheight=0.30)

    def update_canvas(self, event):
        self.canvas.delete("all")

        width = event.width
        height = event.height

        # Desenhar o eixo x
        self.canvas.create_line(0, height / 2, width, height / 2, fill="green")

        # Desenhar o eixo y
        self.canvas.create_line(width / 2, 0, width / 2, height, fill="green")

        # Marcar o ponto de encontro dos eixos
        center_x = width / 2
        center_y = height / 2
        marker_radius = 5
        self.canvas.create_oval(center_x - marker_radius, center_y - marker_radius,
                                center_x + marker_radius, center_y + marker_radius, fill="green")

        # Marcar a coordenada (3, 3)
        coord_x = center_x + self.x1 * (width / 20)
        coord_y = center_y - 0 * (height / 20)
        self.canvas.create_oval(coord_x - marker_radius, coord_y - marker_radius,
                                coord_x + marker_radius, coord_y + marker_radius, fill="red")

        coord_x = center_x + self.x2 * (width / 20)
        coord_y = center_y - 0 * (height / 20)
        self.canvas.create_oval(coord_x - marker_radius, coord_y - marker_radius,
                                coord_x + marker_radius, coord_y + marker_radius, fill="red")

        for x in range(20):
            self.y = (self.a) * (x ** 2) + (self.b * x) + (self.c)
            self.canvas.bind("<Configure>", self.update_canvas)

            coord_x = center_x + x * (width / 20)
            coord_y = center_y - self.y * (height / 20)
            self.canvas.create_oval(coord_x - marker_radius, coord_y - marker_radius,
                                    coord_x + marker_radius, coord_y + marker_radius, fill="red")

    def widgets(self):
        self.Label_a = Label(self.root_bhaskara, text="a:", font=self.fonte_padrao, bg=colors.background1, fg=colors.foreground1)
        self.Label_a.place(relx=0.05, rely=0.05)

        self.Label_b = Label(self.root_bhaskara, text="b:", font=self.fonte_padrao, bg=colors.background1, fg=colors.foreground1)
        self.Label_b.place(relx=0.05, rely=0.15)

        self.Label_c = Label(self.root_bhaskara, text="c:", font=self.fonte_padrao, bg=colors.background1, fg=colors.foreground1)
        self.Label_c.place(relx=0.05, rely=0.25)

        self.Entry_a = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2, fg=colors.foreground1)
        self.Entry_a.place(relx=0.2, rely=0.05, relheight=0.1, relwidth=0.3)

        self.Entry_b = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2, fg=colors.foreground1)
        self.Entry_b.place(relx=0.2, rely=0.15, relheight=0.1, relwidth=0.3)

        self.Entry_c = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2, fg=colors.foreground1)
        self.Entry_c.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.3)

        self.btnCalcular = Button(self.root_bhaskara, text="CALCULAR", command=self.bhaskara_calc,font=fontes.fonte_verdana_bhaskara_button, bg=colors.background2, fg=colors.foreground2)
        self.btnCalcular.place(relx = 0.2, rely=0.40, relheight=0.1, relwidth=0.3)

        self.lbl_resultado = Label(self.root_bhaskara, text="f(x) = ax^2+bx+c", font=self.fonte_padrao, bg=colors.background1, fg=colors.foreground2)
        self.lbl_resultado.place(relx=0.60, rely=0.40)

    def bhaskara_calc(self):
        self.a = int(self.Entry_a.get())
        self.b = int(self.Entry_b.get())
        self.c = int(self.Entry_c.get())
        delta = (self.b**2) - 4 * (self.a) * (self.c)
        if delta < 0:
            print("Delta não possui valor real pois seu delta é menor que 0")
        else:
            #f(x) = ax^2 + bx + c
            raizQ_delta = delta**(1/2)
            self.x1 = (-(self.b)+raizQ_delta) / (2*(self.a))
            self.x2 = (-(self.b)-raizQ_delta) / (2*(self.a))


            self.lbl_resultado["text"] = f"f(x) = {self.a}x^2+{self.b}x + {self.c}\n\nX' = {self.x1} | X'' = {self.x2} "
            print(self.x1, self.x2)
            self.canvas = tkinter.Canvas(self.frm, bg="black")
            self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.canvas.bind("<Configure>", self.update_canvas)


if __name__ == "__main__":
    AppBhaskara()
