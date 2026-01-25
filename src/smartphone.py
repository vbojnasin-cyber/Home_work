from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов, наследник Product"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """
        Инициализация смартфона

        Args:
            name (str): Название
            description (str): Описание
            price (float): Цена
            quantity (int): Количество
            efficiency (str): Производительность
            model (str): Модель
            memory (int): Объем встроенной памяти (в ГБ)
            color (str): Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

    def __str__(self):
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"
            f"Производительность: {self.efficiency}, Модель: {self.model}, "
            f"Память: {self.memory} ГБ, Цвет: {self.color}"
        )
