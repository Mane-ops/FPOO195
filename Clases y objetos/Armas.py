class Armas:
    def seleccionarArma(self, getNombre):
        seleccion = int(input("Selecciona el arma:\n 1 = Rifle de asalto\n 2 = Espada de energia\n 3 = Rifle M392\n"))
        
        if(seleccion == 1):
            print("Rifle de asalto asignado a "+ getNombre())
            print("Municiones 7.62 * 52mm, sin mira")
            
        if(seleccion == 2):
            print("Espada de energia asignada a "+ getNombre())
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            print("Rifle M392 asignado a "+ getNombre())
            print("Municiones 7.62 * 52mm, con mira")
        
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print("arma recargada al "+ str(cargador)+ "%")