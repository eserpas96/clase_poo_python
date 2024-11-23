class Casa:
    def __init__(self, nombre, asentamiento):
        self.nombre = nombre
        self.asentamiento = asentamiento
    
    def __str__(self):
        return (f"Nombre: {self.nombre},"
                + f" Asentamiento: {self.asentamiento}")