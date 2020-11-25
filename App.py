import tkinter as tk
from tkinter import Button, Entry, Label, Menu
import BBDD

class Aplicacion(tk.Frame):

    def __init__(self,master = None):
        self.master = master
        super().__init__(master)
        self.pack()
        self.crear_Widgets()
        self.master.resizable(0,0)
        self.master.title('Login')
        BBDD.basededatos.conexionBD(self)
        

    def crear_Widgets(self):
        self.usernameLabel = Label(self,text='Username')
        self.usernameLabel.grid(row=0,column=0,padx=3,pady=3)

        self.passLabel = Label(self,text='Pass')
        self.passLabel.grid(row=1,column=0,padx=3,pady=3)
        
        self.usernameEntry = Entry(self)
        self.usernameEntry.grid(row=0,column=1)

        self.passEntry = Entry(self)
        self.passEntry.grid(row=1,column=1)

        self.entrarBoton = Button(self,text='Entrar',command=lambda:BBDD.basededatos.verificar_Login(self,self.usernameEntry.get(),self.passEntry.get()))
        self.entrarBoton.grid(row=2,column=1)

root = tk.Tk()
app = Aplicacion(master=root)
app.mainloop()