# interfaz.py

import tkinter as tk
from Fracciones import Fraccion

class Aplicacion:
    def _init_(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Fracciones")

        self.label_numerador1 = tk.Label(ventana, text="Numerador Fracción 1:")
        self.label_numerador1.grid(row=0, column=0)
        self.entry_numerador1 = tk.Entry(ventana)
        self.entry_numerador1.grid(row=0, column=1)

        self.label_denominador1 = tk.Label(ventana, text="Denominador Fracción 1:")
        self.label_denominador1.grid(row=1, column=0)
        self.entry_denominador1 = tk.Entry(ventana)
        self.entry_denominador1.grid(row=1, column=1)

        self.label_numerador2 = tk.Label(ventana, text="Numerador Fracción 2:")
        self.label_numerador2.grid(row=2, column=0)
        self.entry_numerador2 = tk.Entry(ventana)
        self.entry_numerador2.grid(row=2, column=1)

        self.label_denominador2 = tk.Label(ventana, text="Denominador Fracción 2:")
        self.label_denominador2.grid(row=3, column=0)
        self.entry_denominador2 = tk.Entry(ventana)
        self.entry_denominador2.grid(row=3, column=1)

        self.boton_suma = tk.Button(ventana, text="Sumar", command=self.sumar)
        self.boton_suma.grid(row=4, column=0)

        self.boton_resta = tk.Button(ventana, text="Restar", command=self.restar)
        self.boton_resta.grid(row=4, column=1)

        self.boton_multiplicacion = tk.Button(ventana, text="Multiplicar", command=self.multiplicar)
        self.boton_multiplicacion.grid(row=5, column=0)

        self.boton_division = tk.Button(ventana, text="Dividir", command=self.dividir)
        self.boton_division.grid(row=5, column=1)

        self.label_resultado = tk.Label(ventana, text="")
        self.label_resultado.grid(row=6, columnspan=2)

    def sumar(self):
        numerador1 = int(self.entry_numerador1.get())
        denominador1 = int(self.entry_denominador1.get())
        numerador2 = int(self.entry_numerador2.get())
        denominador2 = int(self.entry_denominador2.get())

        fraccion1 = Fraccion(numerador1, denominador1)
        fraccion2 = Fraccion(numerador2, denominador2)

        resultado = fraccion1.suma(fraccion2)
        self.mostrar_resultado(resultado)

    def restar(self):
        numerador1 = int(self.entry_numerador1.get())
        denominador1 = int(self.entry_denominador1.get())
        numerador2 = int(self.entry_numerador2.get())
        denominador2 = int(self.entry_denominador2.get())

        fraccion1 = Fraccion(numerador1, denominador1)
        fraccion2 = Fraccion(numerador2, denominador2)

        resultado = fraccion1.resta(fraccion2)
        self.mostrar_resultado(resultado)

    def multiplicar(self):
        numerador1 = int(self.entry_numerador1.get())
        denominador1 = int(self.entry_denominador1.get())
        numerador2 = int(self.entry_numerador2.get())
        denominador2 = int(self.entry_denominador2.get())

        fraccion1 = Fraccion(numerador1, denominador1)
        fraccion2 = Fraccion(numerador2, denominador2)

        resultado = fraccion1.multiplicacion(fraccion2)
        self.mostrar_resultado(resultado)

    def dividir(self):
        numerador1 = int(self.entry_numerador1.get())
        denominador1 = int(self.entry_denominador1.get())
        numerador2 = int(self.entry_numerador2.get())
        denominador2 = int(self.entry_denominador2.get())

        fraccion1 = Fraccion(numerador1, denominador1)
        fraccion2 = Fraccion(numerador2, denominador2)

        resultado = fraccion1.division(fraccion2)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        self.label_resultado.config(text=f"Resultado: {resultado}")

if __name__ == "_main_":
    ventana_principal = tk.Tk()
    aplicacion = Aplicacion(ventana_principal)
    ventana_principal.mainloop()