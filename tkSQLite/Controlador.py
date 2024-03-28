from tkinter import messagebox
import sqlite3
import bcrypt


class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("C:/Users/maner/OneDrive/Escritorio/POO/FPOO195/tkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se puede conectar")
            
    def encriptapass(self, cont):
        passPlana = cont
        passPlana = passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        
        return passHash
    
    def insertUsuario(self, nom, corr, cont):
        
        conexion = self.conexion()
        
        if(nom == "" or corr == "" or cont==""):
            messagebox.showwarning("Cuidado","Inputs vacios no sea tibio")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH = self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlInsert = "insert into tbUsuarios(nombre,correo,contra) values(?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Eso tilin!!!")
            
    def buscarUsuario(self, id):
        
        conexion = self.conexion()
        
        if(id == ""):
            messagebox.showwarning("Cuidado","Inputs vacios no sea tibio")
            conexion.close()
            
        else:
            try:
                cursor = conexion.cursor()
                sqlSelect = "select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario = cursor.fetchall()
                conexion.close()
                return usuario
                
            except sqlite3.OperationalError:
                print("No se encontró al usuario")
            
    def consultarUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select * from tbUsuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        
        except sqlite3.OperationalError:
            print("Error al consultar usuarios")