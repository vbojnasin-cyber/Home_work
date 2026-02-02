from .base_product import BaseProduct
from .repr_mixin import ReprMixin


class Product(BaseProduct, ReprMixin):  # Миксин идет ПЕРВЫМ!
    def __init__(self, name, description, price, quantity):
        # Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        # Вызываем конструктор всех родителей
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов с проверкой типов"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных категорий")

        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self._BaseProduct__price  # доступ к приватному атрибуту родителя

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Цена не может быть меньше 0")
        else:
            self._BaseProduct__price = new_price
