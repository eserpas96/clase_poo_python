class Producto:
    def __init__(self, clave, nombre, precio, cantidad):
        self.clave = clave
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.precio} x {self.cantidad}"