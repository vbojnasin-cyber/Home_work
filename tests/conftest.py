import pytest

from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Яблоки", description="Фрукты", price=100, quantity=300)


@pytest.fixture
def category():
    return Category("Фрукты", "Свежие фрукты")




@pytest.fixture
def smartphone():
    return Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=89990,
        quantity=50,
        efficiency="A16 Bionic",
        model="15 Pro",
        memory=256,
        color="Титановый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        name="Samsung Galaxy",
        description="Смартфон Samsung",
        price=69990,
        quantity=30,
        efficiency="Snapdragon 8 Gen 2",
        model="S23 Ultra",
        memory=512,
        color="Черный"
    )



@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    Category.category_count = 0
    Category.product_count = 0
    return Category("Тестовая категория", "Описание категории")





