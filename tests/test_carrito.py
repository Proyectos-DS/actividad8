## Ejemplo de prueba
# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00, stock=5)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00, stock=5)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00, stock=3)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


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


def test_vaciar():

    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    carrito.agregar_producto(producto2, cantidad=2)
    producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    carrito.agregar_producto(producto3, cantidad=3)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0
    

def test_aplicar_descuento_condicional_cumplido():

    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 3000)

    # Assert
    assert total_con_descuento == 3230


def test_aplicar_descuento_condicional_no_cumplido():

    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(15, 4000)

    # Assert
    assert total_con_descuento == 3800


    
def test_agregar_producto_hay_stock():
    
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=3800.00, stock=10)

    # Act
    carrito.agregar_producto(producto, cantidad=5)

    # Assert
    assert producto.stock == 5

def test_agregar_producto_supera_stock():
    
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=3800.00, stock=10)

    # Act
    with pytest.raises(ValueError) as excinfo:
        carrito.agregar_producto(producto, cantidad=15)
    # Assert
    assert str(excinfo.value) == f"Cantidad supera a stock de {producto.nombre}, solo hay {producto.stock} unidades"


def test_obtener_items_ordenados_nombre():

    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    carrito.agregar_producto(producto2, cantidad=2)
    producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    carrito.agregar_producto(producto3, cantidad=3)

    # Act
    items_ordenados = carrito.obtener_items_ordenados(criterio='nombre')

    # Assert
    assert items_ordenados[0].producto.nombre == "Audifonos"
    assert items_ordenados[1].producto.nombre == "Laptop"
    assert items_ordenados[2].producto.nombre == "Tablet"


def test_obtener_items_ordenados_precio():

    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    carrito.agregar_producto(producto2, cantidad=2)
    producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    carrito.agregar_producto(producto3, cantidad=3)

    # Act
    items_ordenados = carrito.obtener_items_ordenados(criterio='precio')

    # Assert
    assert items_ordenados[0].producto.precio == 200
    assert items_ordenados[1].producto.precio == 800
    assert items_ordenados[2].producto.precio == 3800


def test_obtener_items_ordenados_criterio_invalido():

    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=3800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Audifonos", precio=200.00)
    carrito.agregar_producto(producto2, cantidad=2)
    producto3 = ProductoFactory(nombre="Tablet", precio=800.00)
    carrito.agregar_producto(producto3, cantidad=3)

    # Act
    criterio = 'marca'
    with pytest.raises(ValueError) as excinfo:
        items_ordenados = carrito.obtener_items_ordenados(criterio=criterio)
    
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