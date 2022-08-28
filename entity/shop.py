from entity.base_storage import BaseStorage
from exceptions import TooManyDifferentProducts


class Shop(BaseStorage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def __str__(self):
        st = f'{self.__class__.__name__}:\n'

        for key, value in self._items.items():
            st += f"{key}: {value}\n"

        st += f'Свободно: {self.get_free_space()}\n'

        return st

    def add(self, title: str, quantity: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(title, quantity)
