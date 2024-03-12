import random
import string
import tkinter as tk
from tkinter import messagebox

class Matricula:
    def __init__(self, nacimiento = "", nombre = "", apep = "", apem = "", carrera = ""):
        self.curso = '2024'
        self.nacimiento = nacimiento
        self.nombre = nombre
        self.apep = apep
        self.apem = apem
        self.carrera = carrera
        
    
    def generador_matricula(self):
        aleatorio = str(random.randrange(1,9))
        aleatorio2 = str(random.randrange(1,9))
        aleatorio3 = str(random.randrange(1,9))
        mat = (self.curso[2:] + self.nacimiento[2:] + self.nombre[:1] + self.apep[:1] + self.apem[:1] + aleatorio + aleatorio2 + aleatorio3 + self.carrera[:3])
        return str(mat)
        
