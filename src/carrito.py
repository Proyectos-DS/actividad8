# src/carrito.py

class Producto:
    def __init__(self, nombre, precio, stock=50):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio})"


class ItemCarrito:
    def __init__(self, producto, cantidad=1):
        self.producto = producto
        self.cantidad = cantidad

    def total(self):
        return self.producto.precio * self.cantidad

    def __repr__(self):
        return f"ItemCarrito({self.producto}, cantidad={self.cantidad})"


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.producto.stock > cantidad:
                    item.cantidad += cantidad
                    item.producto.stock -= cantidad
                    return
                else:
                    raise ValueError(f"Cantidad supera a stock de {item.producto.nombre}, solo hay {item.producto.stock} unidades")
        if producto.stock > cantidad:
            self.items.append(ItemCarrito(producto, cantidad))
            producto.stock -= cantidad
        else:
            raise ValueError(f"Cantidad supera a stock de {producto.nombre}, solo hay {producto.stock} unidades")

    def remover_producto(self, producto, cantidad=1):
        """
        Remueve una cantidad del producto del carrito.
        Si la cantidad llega a 0, elimina el item.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")

    def actualizar_cantidad(self, producto, nueva_cantidad):
        """
        Actualiza la cantidad de un producto en el carrito.
        Si la nueva cantidad es 0, elimina el item.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                else:
                    item.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")

    def calcular_total(self):
        """
        Calcula el total del carrito sin descuento.
        """
        return sum(item.total() for item in self.items)

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al total del carrito y retorna el total descontado.
        El porcentaje debe estar entre 0 y 100.
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def contar_items(self):
        """
        Retorna el número total de items (sumando las cantidades) en el carrito.
        """
        return sum(item.cantidad for item in self.items)

    def obtener_items(self):
        """
        Devuelve la lista de items en el carrito.
        """
        return self.items

    def vaciar(self):
        """Elimina todos los items de la instancia de Carrito
        """
        self.items = []

    def aplicar_descuento_condicional(self, porcentaje, minimo):
        if self.calcular_total() >= minimo:
            return self.aplicar_descuento(porcentaje)
        else:
            return self.calcular_total()

    
    def obtener_items_ordenados(self, criterio: str):
        # criterios = {'nombre': 0, 'precio': 1}
        if criterio == 'nombre':
            sorted_items = sorted(self.items, key=lambda x:x.producto.nombre)
            return sorted_items
        elif criterio == 'precio':
            sorted_items = sorted(self.items, key=lambda x:x.producto.precio)
            return sorted_items
        else:
            raise ValueError(f"Criterio '{criterio}' invalido")