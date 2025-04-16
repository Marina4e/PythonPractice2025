class Singleton:
    _instance = None  # Статичне поле, що зберігає єдиний екземпляр класу

    def __new__(cls):
        # Перевіряємо, чи був екземпляр вже створений
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Перевіряємо роботу Singleton
singleton1 = Singleton()
singleton2 = Singleton()

# Порівнюємо екземпляри
print(f"singleton1 is singleton2: {singleton1 is singleton2}")
# Виведе True, оскільки обидва екземпляри посилаються на один і той самий об'єкт
