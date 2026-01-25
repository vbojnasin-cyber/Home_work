from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{self.name} ({self.model}), {self.price} руб. "
                f"Остаток: {self.quantity} шт. "
                f"Память: {self.memory} ГБ, Цвет: {self.color}")