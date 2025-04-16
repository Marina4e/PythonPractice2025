from abc import ABC, abstractmethod


# Абстрактний клас продукту
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретні продукти
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProductB"


# Абстрактний клас створювача
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()  # Використовуємо продукт, створений підкласом
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


# Конкретні створювачі
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


# Приклад використання
def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}")


# Тестування
print("App: Launched with the ConcreteCreatorA.")
client_code(ConcreteCreatorA())

print("\nApp: Launched with the ConcreteCreatorB.")
client_code(ConcreteCreatorB())
