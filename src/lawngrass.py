from .product import Product


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        # Вызов родительского конструктора с проверкой quantity
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
            f"Страна: {self.country}, "
            f"Срок прорастания: {self.germination_period} дней, "
            f"Цвет: {self.color}"
        )
