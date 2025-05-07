## Ejemplo de prueba
# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo(carrito_vacio):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito_vacio.agregar_producto(producto)
    
    # Assert
    items = carrito_vacio.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito_vacio, producto_tablet):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    # carrito = Carrito()
    # producto = ProductoFactory(nombre="Mouse", precio=50.00, stock=10)
    # carrito.agregar_producto(producto, cantidad=1)
    carrito_vacio.agregar_producto(producto_tablet, 3)
    
    # Act
    # carrito.agregar_producto(producto, cantidad=2)
    carrito_vacio.agregar_producto(producto_tablet, 4) 

    
    # Assert
    items = carrito_vacio.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 7


def test_remover_producto(carrito_vacio, producto_laptop):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    # carrito = Carrito()
    # producto = ProductoFactory(nombre="Teclado", precio=75.00, stock=5)
    # carrito.agregar_producto(producto, cantidad=3)
    carrito_vacio.agregar_producto(producto_laptop, cantidad=3)
    
    # Act
    # carrito.remover_producto(producto, cantidad=1)
    carrito_vacio.remover_producto(producto_laptop, cantidad=1)
    
    # Assert
    # items = carrito.obtener_items()
    items = carrito_vacio.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito_vacio, producto_tablet):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    # carrito = Carrito()
    # producto = ProductoFactory(nombre="Monitor", precio=300.00)
    # carrito.agregar_producto(producto, cantidad=2)
    carrito_vacio.agregar_producto(producto_tablet, cantidad=2)
    
    # Act
    # carrito.remover_producto(producto, cantidad=2)
    carrito_vacio.remover_producto(producto_tablet, cantidad=2)
    
    # Assert
    # items = carrito.obtener_items()
    items = carrito_vacio.obtener_items()
    assert len(items) == 0
    


def test_actualizar_cantidad_producto(carrito_vacio, producto_audifonos):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    # carrito = Carrito()
    # producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    # carrito.agregar_producto(producto, cantidad=1)
    carrito_vacio.agregar_producto(producto_audifonos, cantidad=1)
    
    # Act
    # carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    carrito_vacio.actualizar_cantidad(producto_audifonos, nueva_cantidad=5)
    
    # Assert
    # items = carrito.obtener_items()
    items = carrito_vacio.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito_vacio, producto_audifonos):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    # carrito = Carrito()
    # producto = ProductoFactory(nombre="Cargador", precio=25.00, stock=5)
    # carrito.agregar_producto(producto, cantidad=3)
    carrito_vacio.agregar_producto(producto_audifonos, cantidad=3)
    
    # Act
    #carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    carrito_vacio.actualizar_cantidad(producto_audifonos, nueva_cantidad=0)
    
    # Assert
    # items = carrito.obtener_items()
    items = carrito_vacio.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito_con_productos):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    # carrito = Carrito()
    # producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    # producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    # carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    # carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    total_carrito_con_productos = 10400.00


    # Act
    # total = carrito.calcular_total()
    total = carrito_con_productos.calcular_total()
    
    # Assert
    assert total == total_carrito_con_productos

@pytest.mark.parametrize(
        "cantidad, porcentaje_descuento, total_esperado", 
        [(2, 10, 1440.00), (3, 20, 1920)]
)
def test_aplicar_descuento(carrito_vacio, producto_tablet, cantidad, porcentaje_descuento, total_esperado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad de 2 y 3.
    Act: Se aplica un descuento del 10% y 15% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito_vacio.agregar_producto(producto_tablet, cantidad=cantidad)
    
    # Act
    total_con_descuento = carrito_vacio.aplicar_descuento(porcentaje_descuento)
    
    # Assert
    assert total_con_descuento == total_esperado


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_vaciar(carrito_con_productos):

    # Arrange
    assert carrito_con_productos.contar_items() > 0

    # Act
    carrito_con_productos.vaciar()

    # Assert
    assert carrito_con_productos.obtener_items() == []
    assert carrito_con_productos.calcular_total() == 0
    assert carrito_con_productos.contar_items() == 0
    
@pytest.mark.parametrize(
        "porcentaje_descuento, compra_minima, total_esperado",
        [
            (15, 3000, 8840.00), 
            (20, 10000, 8320.00)
        ]
)
def test_aplicar_descuento_condicional_cumplido(carrito_con_productos, 
                                                porcentaje_descuento, 
                                                compra_minima,
                                                total_esperado):
    """
    AAA (parametrizado)
    Arrange: carrito_con_productos tiene un valor total de 10400
    Act: aplicamos el descuento
    Assert: Validamos que la cantidad final corresponda con el descuento aplicado
    """
    # Arrange
    assert carrito_con_productos.calcular_total() > 0

    # Act
    total_con_descuento = carrito_con_productos.aplicar_descuento_condicional(porcentaje_descuento, compra_minima)

    # Assert
    assert total_con_descuento == total_esperado


def test_aplicar_descuento_condicional_no_cumplido(carrito_con_productos):

    # Arrange
    total_sin_descuento = carrito_con_productos.calcular_total()

    # Act
    total_con_descuento = carrito_con_productos.aplicar_descuento_condicional(15, 12000)

    # Assert
    assert total_con_descuento == total_sin_descuento



def test_agregar_producto_supera_stock(carrito_vacio, producto_tablet):
    
    # Arrange
    nombre_producto_tablet = producto_tablet.nombre
    stock_producto_tablet = producto_tablet.stock
    cantidad = stock_producto_tablet + 1

    # Act
    with pytest.raises(ValueError) as excinfo:
        carrito_vacio.agregar_producto(producto_tablet, cantidad=cantidad)
    # Assert
    assert str(excinfo.value) == f"Cantidad supera a stock de {nombre_producto_tablet}, solo hay {stock_producto_tablet} unidades"


def test_obtener_items_ordenados_nombre(carrito_con_productos):

    # Arrange
    assert carrito_con_productos.contar_items() > 0
    # Acts
    items_ordenados = carrito_con_productos.obtener_items_ordenados(criterio='nombre')

    # Assert
    assert items_ordenados[0].producto.nombre == "Audifonos"
    assert items_ordenados[1].producto.nombre == "Laptop"
    assert items_ordenados[2].producto.nombre == "Tablet"


def test_obtener_items_ordenados_precio(carrito_con_productos):

    # Arrange
    # carrito = Carrito()
    # producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    # carrito.agregar_producto(producto1, cantidad=1)
    # producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    # carrito.agregar_producto(producto2, cantidad=2)
    # producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    # carrito.agregar_producto(producto3, cantidad=3)
    assert carrito_con_productos.contar_items() > 0

    # Act
    # items_ordenados = carrito.obtener_items_ordenados(criterio='precio')
    items_ordenados = carrito_con_productos.obtener_items_ordenados(criterio='precio')

    # Assert
    assert items_ordenados[0].producto.precio == 200
    assert items_ordenados[1].producto.precio == 800
    assert items_ordenados[2].producto.precio == 3800


def test_obtener_items_ordenados_criterio_invalido(carrito_con_productos):

    # Arrange
    # carrito = Carrito()
    # producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    # carrito.agregar_producto(producto1, cantidad=1)
    # producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    # carrito.agregar_producto(producto2, cantidad=2)
    # producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    # carrito.agregar_producto(producto3, cantidad=3)
    assert carrito_con_productos.contar_items() > 0

    # Act
    criterio = 'marca'
    with pytest.raises(ValueError) as excinfo:
        items_ordenados = carrito_con_productos.obtener_items_ordenados(criterio=criterio)
    
    # Assert
    assert str(excinfo.value) == f"Criterio '{criterio}' invalido"


def prueba():
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    carrito.agregar_producto(producto2, cantidad=2)
    producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    carrito.agregar_producto(producto3, cantidad=3)

    items = carrito.obtener_items()
    print(f"Tipo de elemento: {type(items[0])}")
    print(f"Tipo de elemento dentro 1: {type(items[0].producto)}")
    print(f"Tipo de elemento dentro 1 - 1: {type(items[0].producto.nombre)}")
    print(f"Tipo de elemento dentro 1 - 1: {type(items[0].producto.precio)}")
    print(f"Tipo de elemento dentro 2: {type(items[0].cantidad)}")
    print(f"Items:\n {items}")
    print("Items ordenados")
    sort_items = carrito.obtener_items_ordenados('nombre')
    print(sort_items)

if __name__=="__main__":
    prueba()