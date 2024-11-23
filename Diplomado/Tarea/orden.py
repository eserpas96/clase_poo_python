class Orden:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.cantidad
        return total

    def __str__(self):
        return '\n'.join(str(producto) for producto in self.productos)