import pytest
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.category import Category


class TestIntegration:
    """Интеграционные тесты взаимодействия классов"""

    def test_add_and_str_integration(self):
        """Интеграционный тест: создание, добавление, вывод"""
        # Создаем продукты
        phone = Smartphone(
            name="Google Pixel",
            description="Смартфон Google",
            price=65000,
            quantity=15,
            efficiency="Tensor G3",
            model="8 Pro",
            memory=256,
            color="Серый"
        )

        grass = LawnGrass(
            name="Газон Спорт",
            description="Трава для спортивных площадок",
            price=1800,
            quantity=120,
            country="Нидерланды",
            germination_period=12,
            color="Темно-зеленый"
        )

        # Создаем категории
        electronics = Category("Электроника", "Техника")
        garden = Category("Сад", "Садовые товары")

        # Добавляем продукты
        electronics.add_product(phone)
        garden.add_product(grass)

        # Проверяем
        assert len(electronics._Category__products) == 1
        assert len(garden._Category__products) == 1

        # Проверяем строковые представления
        assert "Google Pixel" in str(electronics.products)
        assert "8 Pro" in str(electronics.products)
        assert "Газон Спорт" in str(garden.products)
        assert "Нидерланды" in str(garden.products)

    def test_addition_restrictions(self):
        """Тест ограничений на сложение"""
        phone1 = Smartphone("Тел1", "Описание", 100, 5, "a", "m", 64, "black")
        phone2 = Smartphone("Тел2", "Описание", 200, 3, "b", "n", 128, "white")
        grass = LawnGrass("Трава", "Описание", 50, 10, "RU", 14, "green")

        # Можно складывать одинаковые типы
        result1 = phone1 + phone2
        assert result1 == (100 * 5 + 200 * 3)

        result2 = grass + grass
        assert result2 == (50 * 10 + 50 * 10)

        # Нельзя складывать разные типы
        with pytest.raises(TypeError):
            phone1 + grass

        with pytest.raises(TypeError):
            grass + phone2