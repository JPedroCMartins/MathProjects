import tkinter
from tkinter import *

class AppBhaskara():
    def __init__(self):
        self.root = tkinter.Tk()
        self.tela()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.geometry("480x500")
        pass
    def widgets(self):
        Label_a = Label(self.root, text="a:")
        Label_a.place(relx=0.05, rely=0.05)

        Label_b = Label(self.root, text="b:")
        Label_b.place(relx=0.05, rely=0.15)

        Label_c = Label(self.root, text="c:")
        Label_c.place(relx=0.05, rely=0.25)

        Entry_a = Entry(self.root)
        Entry_a.place(relx=0.2, rely=0.05, relheight=0.1)

        Entry_b = Entry(self.root)
        Entry_b.place(relx=0.2, rely=0.15, relheight=0.1)

        Entry_c = Entry(self.root)
        Entry_c.place(relx=0.2, rely=0.25, relheight=0.1)

if __name__ == "__main__":
    AppBhaskara()
