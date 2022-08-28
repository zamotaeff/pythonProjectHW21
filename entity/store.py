from entity.storage import Storage


class Store(Storage):

    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def __str__(self):
        st = "На складе:\n"

        for key, value in self.items.items():
            st += f"{key}: {value}\n"

        st += f'Свободно: {self.get_free_space()}\n'

        return st

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, quantity):
        if title in self.items.keys():
            if self.get_free_space() >= quantity:
                print(f'Товар {title} в кол-ве {quantity} добавлен на склад/магазин\n')
                self.items[title] += quantity
                return True
            else:
                print("Недостаточно места на складе/магазине!\n")
                return False
        else:
            if self.get_free_space() >= quantity:
                print(f'Товар {title} в кол-ве {quantity} добавлен на склад/магазин\n')
                self.items[title] = quantity
                return True
            else:
                print("Недостаточно места на складе/магазине!\n")
                return False

    def remove(self, title, quantity):
        if self.items[title] >= quantity:
            print("Такое количество товара на складе/магазине есть")
            self.items[title] -= quantity
            return True
        else:
            print("Недостаточно места на складе/магазине")
            return False

    def get_free_space(self):
        current_space = 0

        for value in self.items.values():
            current_space += value

        return self.capacity - current_space

    def get_unique_items_count(self):
        return len(self.items.keys())
