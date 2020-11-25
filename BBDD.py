import sqlite3
from tkinter import messagebox

class basededatos:

    def conexionBD(self):
        
        try:
            self.conexion = sqlite3.connect('Login')
            self.cursor = self.conexion.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50),PASSWORD VARCHAR(50))')
        except:
            messagebox.showerror('Hubo un error')
        finally:
            self.conexion.close()

    def verificar_Login(self,username,password):
        try:
            self.conexion = sqlite3.connect('Login')
            self.cursor = self.conexion.cursor()
            self.registro = (username,password)
            self.cursor.execute('SELECT USERNAME, PASSWORD FROM USER WHERE USERNAME = ? AND PASSWORD = ?',self.registro)
            self.datos = self.cursor.fetchall()
            if self.datos:
                messagebox.showinfo('Funciona','Lo de arriba')
        except:
            messagebox.showerror('Hubo un error')
        finally:
    
            self.conexion.close()