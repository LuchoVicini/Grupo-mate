from tkinter import *

def creacion_ventana():
    raiz= Tk()

    raiz.title("Login Grupo II")
    raiz.resizable(0,0)
    raiz.geometry("300x130")
    raiz.iconbitmap("mate.ico")
    raiz.config(bg="lightblue")

    usuario_label= Label(raiz,text="Usuario Alumno: ")
    usuario_label.place(x=5, y=20)
    clave_label= Label(raiz,text="Clave:")
    clave_label.place(x=5,y=50)
    
    usuario_entry= Entry(raiz)
    usuario_entry.place(x=130,y=20)
    clave_entry= Entry(raiz)
    clave_entry.place(x=130,y=50)
    clave_entry.config(show="*")
    
    ingresar_boton= Button(raiz,text="Ingresar")
    ingresar_boton.place(x=130,y=100)
    
    raiz.mainloop()
    
creacion_ventana()