from abc import ABC, abstractmethod


# Статичний Factory Method – Реальне застосування
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


# Абстрактний клас фабрики
class ProductFactory(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass


# Конкретні фабрики
class ConcreteFactoryA(ProductFactory):
    def create_product(self) -> Product:
        return ConcreteProductA()


class ConcreteFactoryB(ProductFactory):
    def create_product(self) -> Product:
        return ConcreteProductB()


# Використання Factory Method через інтерфейс
def client_code(factory: ProductFactory) -> None:
    product = factory.create_product()
    print(f"Client: The product operation result is: {product.operation()}")


factory_a = ConcreteFactoryA()
client_code(factory_a)  # Output: Client: The product operation result is: Result of the ConcreteProductA
factory_b = ConcreteFactoryB()
client_code(factory_b)  # Output: Client: The product operation result is: Result of the ConcreteProductB
