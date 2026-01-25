from src.product import Product


class Category:
    name: str
    description: str
    products: None
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """
        Добавляет продукт в категорию

        Args:
            product: Объект для добавления

        Raises:
            TypeError: Если передан не объект класса Product или его наследников
        """
        # Используем isinstance() для проверки
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        # Дополнительная проверка с помощью issubclass()
        if not issubclass(type(product), Product):
            raise TypeError(
                "Объект должен быть наследником класса Product"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result