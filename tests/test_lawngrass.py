import pytest

from src.lawngrass import LawnGrass
from src.product import Product


@pytest.fixture
def lawngrass():
    return LawnGrass(
        name="Газонная трава Премиум",
        description="Трава для элитного газона",
        price=2500,
        quantity=150,
        country="Германия",
        germination_period=10,
        color="Изумрудный",
    )


@pytest.fixture
def lawngrass2():
    return LawnGrass(
        name="Газонная трава Стандарт",
        description="Обычная газонная трава",
        price=1200,
        quantity=300,
        country="Россия",
        germination_period=14,
        color="Зеленый",
    )


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawngrass_inheritance(self, lawngrass):
        """Тест: LawnGrass наследуется от Product"""
        assert isinstance(lawngrass, LawnGrass)
        assert isinstance(lawngrass, Product)

    def test_lawngrass_attributes(self, lawngrass):
        """Тест атрибутов LawnGrass"""
        assert lawngrass.name == "Газонная трава Премиум"
        assert lawngrass.description == "Трава для элитного газона"
        assert lawngrass.price == 2500
        assert lawngrass.quantity == 150
        assert lawngrass.country == "Германия"
        assert lawngrass.germination_period == 10
        assert lawngrass.color == "Изумрудный"

    def test_lawngrass_str_method(self, lawngrass):
        """Тест строкового представления"""
        result = str(lawngrass)
        assert "Газонная трава Премиум" in result
        assert "2500" in result  # цена
        assert "150" in result  # количество
        assert "Германия" in result  # страна
        assert "10" in result  # срок прорастания

    def test_lawngrass_addition_same_type(self, lawngrass, lawngrass2):
        """Тест сложения двух газонов"""
        result = lawngrass + lawngrass2
        expected = (2500 * 150) + (1200 * 300)
        assert result == expected

    def test_lawngrass_addition_different_type(self, lawngrass):
        """Тест: нельзя сложить траву с другим типом продукта"""
        from src.smartphone import Smartphone

        phone = Smartphone("Телефон", "Описание", 100, 5, "a", "m", 64, "black")

        with pytest.raises(TypeError) as exc_info:
            lawngrass + phone

        assert "Нельзя складывать товары разных категорий" in str(exc_info.value)

    def test_lawngrass_negative_germination_period(self):
        """Тест: отрицательный срок прорастания (если нужно валидировать)"""
        # Сейчас можно создать с отрицательным сроком, но можно добавить проверку
        grass = LawnGrass("Трава", "Описание", 100, 10, "RU", -5, "Зеленый")
        assert grass.germination_period == -5  # Пока что допустимо
