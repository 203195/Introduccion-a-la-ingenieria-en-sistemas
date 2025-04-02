class Carrito:
    def __init__(self):
        self.productos = {}
        self.cantidad = 0
        self.total = 0
        self.cap_max = 10

    def agregar_producto(self, nombre, precio, cantidad = 1):
        if self.cantidad + cantidad > self.cap_max:
            print(f"No se pueden agregar {cantidad} unidades. Carrito lleno")
            return
        
        if nombre in self. productos:
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'precio': precio, 'cantidad': cantidad}
    
        self.cantidad += cantidad
        self.total += precio * cantidad

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            producto = self.productos[nombre]
            self.cantidad -= producto['cantidad']
            self.total -= producto['precio'] * producto['cantidad']
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado del carrito.")
        else:
            print(f"El producto '{nombre}' no está en el carrito.")

    def pagar(self, monto):
        if monto < self.total:
            print("Monto insuficiente para realizar el pago.")
            return None
        cambio = monto - self.total
        self.productos.clear()
        self.cantidad = 0
        self.total = 0
        print(f"Pago realizado. Su cambio es: ${cambio}")
        return cambio

    def pago_con_tarjeta(self, numero_tarjeta, monto):
        if len(str(numero_tarjeta)) != 16:
            print("Número de tarjeta inválido.")
            return False
        if monto < self.total:
            print("Monto insuficiente para realizar el pago.")
            return False
        self.productos.clear()
        self.cantidad = 0
        self.total = 0
        print("Pago con tarjeta realizado exitosamente.")
        return True

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Porcentaje de descuento inválido.")
            return
        descuento = self.total * (porcentaje / 100)
        self.total -= descuento
        print(f"Descuento del {porcentaje}% aplicado. Total a pagar ahora es: ${self.total:.2f}")

    def mostrar(self):
        print("\n==== CARRITO ====")
        print(self.productos)
        print(f"Total de productos: {self.cantidad} - Total a pagar: ${self.total}")

carrito = Carrito()
carrito.agregar_producto("Leche", 35)
carrito.mostrar()
carrito.agregar_producto("Leche", 35, 4)
carrito.mostrar()
carrito.eliminar_producto("Leche")
carrito.mostrar()
carrito.agregar_producto("Pan", 20, 2)
carrito.mostrar()
carrito.aplicar_descuento(10)
carrito.mostrar()
carrito.pagar(200)
carrito.pago_con_tarjeta(1234567812345678, 200)