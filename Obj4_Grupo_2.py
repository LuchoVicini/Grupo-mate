from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves():
    diccionario= {
        "Luciano":"lucho123",
        "Flor":"flor22",
        "Cinthia":"cinthia19",
        "Bautista":"3123#J",
        "Valentin":"matesito123"
                }
    return diccionario
    
def login_popup(usuario_entry,clave_entry):
    dicc= obtener_usuarios_claves()
    resultado= False
    for n in dicc:
        if usuario_entry== n and clave_entry==dicc[n]:
            resultado= True
    if resultado:
        messagebox.showinfo(message="Usuario y Clave Correctos")
    else:
        messagebox.showerror(message="Algunos de los datos ingresados es incorrecto")
        
    return resultado

def creacion_ventana():
    raiz= Tk()
    
    raiz.title("Login Grupo II")
    raiz.resizable(0,0)
    raiz.geometry("300x130")
    raiz.iconbitmap("Interfaz Grafica\PROYECTO GRUPAL\mate.ico")
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
    
    ingresar_boton= Button(raiz,text="Ingresar",command= lambda:login_popup(usuario_entry.get(),clave_entry.get()))
    ingresar_boton.place(x=130,y=100)
    
    raiz.mainloop()

creacion_ventana()