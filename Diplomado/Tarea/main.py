from producto import Producto
from orden import Orden

# Crear productos
producto1 = Producto(1, "Manzana", 1.5, 10)
producto2 = Producto(2, "Pera", 2.0, 5)
producto3 = Producto(3, "Banana", 0.5, 20)

# Crear una orden
orden = Orden()
orden.agregar_producto(producto1)
orden.agregar_producto(producto2)
orden.agregar_producto(producto3)

# Mostrar productos
print("Lista de productos en la orden:")
print(orden)

# Calcular y mostrar el total de la orden
total = orden.calcular_total()
print(f"\nTotal de la orden: {total}")