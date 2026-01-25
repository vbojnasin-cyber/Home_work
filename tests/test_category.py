from src.category import Category


def test_category_creation(category):
    """Тест 1: Создание категории"""
    assert category.name == "Фрукты"
    assert category.description == "Свежие фрукты"


def test_add_product_to_category(category, product):
    """Тест 2: Добавление продукта в категорию"""
    category.add_product(product)
    assert "Яблоки" in category.products  # проверяем через property


def test_category_str(category, product):
    """Тест 3: Строковое представление категории"""
    category.add_product(product)
    assert "количество продуктов 300" in str(category)


def test_category_counters():
    """Тест 4: Счетчики категорий"""
    Category.category_count = 0  # сброс
    cat1 = Category("Грибы", "Свежие грибы")
    cat2 = Category("Кат2", "Описание2")
    assert Category.category_count == 2


def test_private_products_access(category, product):
    """Тест 5: Приватный список продуктов"""
    category.add_product(product)
    assert len(category._Category__products) == 1
