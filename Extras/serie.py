class Serie:
    def __init__(self, titulo, genero, horas_estimadas=10):
        self.__titulo = titulo
        self.__horas_estimadas = horas_estimadas
        self.__status = "Sin reproducir"
        self.__genero = genero
        self.__calificacion = None

    def reproducir(self):
        return f"Reproduciendo {self.__titulo}"

    def agregar_a_lista(self):
        return f"Agregando {self.__titulo} a mi lista"

    def marcar_como_completada(self):
        self.__status = "Completada"

    def calificar(self, calificacion):
        self.__calificacion = calificacion
