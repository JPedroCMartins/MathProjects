import tkinter
from tkinter import *
from Style import fontes
class AppBhaskara():
    def __init__(self):
        self.root = tkinter.Tk()
        self.fonte_padrao = fontes.fonte_verdana_bhaskara_label
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("480x500")
        pass
    def widgets(self):
        Label_a = Label(self.root, text="a:", font=self.fonte_padrao)
        Label_a.place(relx=0.05, rely=0.05)

        Label_b = Label(self.root, text="b:", font=self.fonte_padrao)
        Label_b.place(relx=0.05, rely=0.15)

        Label_c = Label(self.root, text="c:", font=self.fonte_padrao)
        Label_c.place(relx=0.05, rely=0.25)

        Entry_a = Entry(self.root, font=self.fonte_padrao)
        Entry_a.place(relx=0.2, rely=0.05, relheight=0.1, relwidth=0.3)

        Entry_b = Entry(self.root, font=self.fonte_padrao)
        Entry_b.place(relx=0.2, rely=0.15, relheight=0.1, relwidth=0.3)

        Entry_c = Entry(self.root, font=self.fonte_padrao)
        Entry_c.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.3)

        btnCalcular = Button(text="Calcular", font=self.fonte_padrao)
        btnCalcular.place(relx = 0.2, rely=0.40, relheight=0.1, relwidth=0.3)

if __name__ == "__main__":
    AppBhaskara()
