from abc import ABC, abstractmethod


# Абстрактний клас продукту
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретні продукти
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "ConcreteProductA operation"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "ConcreteProductB operation"


# Статичний Factory Method
class StaticFactory:
    @staticmethod
    def create_product(type: str) -> Product:
        if type == "A":
            return ConcreteProductA()
        elif type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Unknown product type")


# Приклад використання
def static_factory_client():
    product_a = StaticFactory.create_product("A")
    print(product_a.operation())  # Виведе: ConcreteProductA operation

    product_b = StaticFactory.create_product("B")
    print(product_b.operation())  # Виведе: ConcreteProductB operation


static_factory_client()
