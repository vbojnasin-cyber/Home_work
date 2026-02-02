import pytest

from src.product import Product
from src.smartphone import Smartphone




class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_inheritance(self, smartphone):
        """Тест: Smartphone наследуется от Product"""
        assert isinstance(smartphone, Smartphone)
        assert isinstance(smartphone, Product)

    def test_smartphone_attributes(self, smartphone):
        """Тест атрибутов Smartphone"""
        assert smartphone.name == "iPhone 15"
        assert smartphone.description == "Смартфон Apple"
        assert smartphone.price == 89990
        assert smartphone.quantity == 50
        assert smartphone.efficiency == "A16 Bionic"
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 256
        assert smartphone.color == "Титановый"

    def test_smartphone_str_method(self, smartphone):
        """Тест строкового представления"""
        result = str(smartphone)
        assert "iPhone 15" in result
        assert "15 Pro" in result  # модель
        assert "256" in result  # память
        assert "Титановый" in result  # цвет
        assert "89990" in result  # цена

    def test_smartphone_addition_same_type(self, smartphone, smartphone2):
        """Тест сложения двух смартфонов"""
        result = smartphone + smartphone2
        expected = (89990 * 50) + (69990 * 30)
        assert result == expected

    def test_smartphone_addition_different_type(self, smartphone):
        """Тест: нельзя сложить смартфон с другим типом продукта"""
        from src.lawngrass import LawnGrass
        grass = LawnGrass("Трава", "Описание", 100, 10, "RU", 14, "Зеленый")

        with pytest.raises(TypeError) as exc_info:
            smartphone + grass

        assert "Нельзя складывать товары разных категорий" in str(exc_info.value)

    def test_smartphone_price_setter(self, smartphone):
        """Тест сеттера цены (унаследован от Product)"""
        smartphone.price = 85000
        assert smartphone.price == 85000

        # Проверка на отрицательную цену
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        smartphone.price = -100

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert "Цена не может быть меньше 0" in output
        assert smartphone.price == 85000  # цена не изменилась


def test_smartphone_new_product_method():
    """Тест классового метода new_product для Smartphone"""
    product_data = {
        "name": "Xiaomi Phone",
        "description": "Китайский смартфон",
        "price": 35000,
        "quantity": 25,
        "efficiency": "Snapdragon 888",
        "model": "13 Pro",
        "memory": 128,
        "color": "Синий"
    }

    smartphone = Smartphone(**product_data)

    assert smartphone.name == "Xiaomi Phone"
    assert smartphone.model == "13 Pro"
    assert smartphone.memory == 128