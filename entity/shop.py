from entity.store import Store


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def __str__(self):
        st = "В магазине:\n"

        for key, value in self.items.items():
            st += f"{key}: {value}\n"

        st += f'Свободно: {self.get_free_space()}\n'

        return st

    def add(self, title, quantity):
        if self.get_unique_items_count() >= 5:
            print("Cлишком много разных товаров\n")
            return False
        else:
            super().add(title, quantity)
