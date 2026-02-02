class ReprMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")

    def __repr__(self):
        attrs = []
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                attrs.append(f"{key}={repr(value)}")

        class_name = self.__class__.__name__
        return f"{class_name}({', '.join(attrs)})"
