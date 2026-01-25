from src.product import Product


def test_new_product(product):
    assert product.quantity == 300
    assert product.price == 100
    assert product.name == "Яблоки"
    assert product.description == "Фрукты"

    assert product._Product__price == 100


def test_price_setter(product):
    product.price = 150
    assert product.price == 150


def test_product_add(product):
    product_2 = Product("Груши", "Фрукты", 200, 50)
    result = product + product_2
    assert result == 40000


def test_new_product_from_dict():
    product_data = {
        "name": "banana",
        "description": "fruit",
        "price": 400,
        "quantity": 100,
    }
    product_4 = Product.new_product(product_data)
    assert product_4.name == "banana"
    assert product_4.description == "fruit"
    assert product_4.price == 400
    assert product_4.quantity == 100
