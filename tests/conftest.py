import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito_vacio():
    return Carrito()


@pytest.fixture
def producto_generico():
    return ProductoFactory(nombre="Generico", precio=100.00, stock=50)

@pytest.fixture
def producto_laptop():
    """
    Returns:
        Producto: (nombre="Laptop", precio=3800, stock=50
    """
    return ProductoFactory(nombre="Laptop", precio=3800, stock=50)

@pytest.fixture
def producto_tablet():
    return ProductoFactory(nombre="Tablet", precio=800, stock=50)

@pytest.fixture
def producto_audifonos():
    return ProductoFactory(nombre="Audifonos", precio=200, stock=80)

@pytest.fixture
def carrito_con_productos(carrito_vacio, producto_laptop, producto_tablet, producto_audifonos):
    carrito_vacio.agregar_producto(producto_laptop, 1)
    carrito_vacio.agregar_producto(producto_tablet, 3)
    carrito_vacio.agregar_producto(producto_audifonos, 2)
    return carrito_vacio