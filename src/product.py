class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
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
            print("Цена не может быть меньше 0")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов с проверкой типов"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        # Проверяем, что объекты одного конкретного класса
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных категорий")

        return self.price * self.quantity + other.price * other.quantity

