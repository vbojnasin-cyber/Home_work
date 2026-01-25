class Product:
    # Придаем тип обьектам
    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name, description, price, quantity
    ):  # Создаем конструктор класса
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не должна быть 0 или меньше")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name} по цене {self.price} рублей - кол-во {self.quantity} штук"

    def __add__(self, other):
        """Сложение продуктов(price_1 * quantity_1 + price_2 * quantity_2)"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только обьекты класса Product")
        return self.price * self.quantity + other.price * other.quantity


product_1 = Product("Яблоки", "fruits", 100, 300)
print(product_1)
