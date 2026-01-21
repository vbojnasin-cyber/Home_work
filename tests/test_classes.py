import pytest

from src.classes import Product, Category


class TestProduct:
    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_addition(self):
        """Тест сложения двух продуктов"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой", 100000.0, 2)

        # 50000 * 10 + 100000 * 2 = 500000 + 200000 = 700000
        result = product1 + product2
        assert result == 700000.0

    def test_product_addition_wrong_type(self):
        """Тест сложения с неправильным типом"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
            product + 100

    def test_price_setter_valid(self):
        """Тест сеттера цены с валидным значением"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = 45000.0
        assert product.price == 45000.0

    def test_price_setter_invalid(self, capsys):
        """Тест сеттера цены с невалидным значением"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = -100

        # Проверяем, что цена не изменилась
        assert product.price == 50000.0

        # Проверяем вывод сообщения об ошибке
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out


class TestCategory:
    def test_category_str_empty(self):
        """Тест строкового представления пустой категории"""
        category = Category("Электроника", "Электронные устройства")
        expected = "Электроника, количество продуктов: 0 шт."
        assert str(category) == expected

    def test_category_str_with_products(self):
        """Тест строкового представления категории с товарами"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой", 100000.0, 2)

        category = Category("Электроника", "Электронные устройства", [product1, product2])
        expected = "Электроника, количество продуктов: 12 шт."
        assert str(category) == expected

    def test_products_getter(self):
        """Тест геттера для списка продуктов"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой", 100000.0, 2)

        category = Category("Электроника", "Электронные устройства", [product1, product2])

        products_str = category.products
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in products_str
        assert "Ноутбук, 100000.0 руб. Остаток: 2 шт." in products_str

    def test_add_product(self):
        """Тест добавления товара в категорию"""
        category = Category("Электроника", "Электронные устройства")
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        category.add_product(product)

        # Проверяем, что продукт добавился
        assert len(category._Category__products) == 1
        assert str(product) in category.products


class TestNewProduct:
    def test_new_product_from_dict(self):
        """Тест создания продукта из словаря"""
        product_data = {
            "name": "Телефон",
            "description": "Смартфон",
            "price": 50000.0,
            "quantity": 10
        }

        product = Product.new_product(product_data)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10


if __name__ == "__main__":
    # Запуск тестов
    pytest.main([__file__, "-v"])