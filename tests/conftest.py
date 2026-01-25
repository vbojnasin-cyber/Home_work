import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Яблоки", description="Фрукты", price=100, quantity=300)


@pytest.fixture
def category():
    return Category("Фрукты", "Свежие фрукты")
