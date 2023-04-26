from tkinter import *

def creacion_ventana():
    raiz= Tk()

    raiz.title("Login Grupo II")
    raiz.resizable(0,0)
    raiz.geometry("300x130")
    raiz.iconbitmap("mate.ico")
    raiz.config(bg="lightblue")

    raiz.mainloop()

creacion_ventana()