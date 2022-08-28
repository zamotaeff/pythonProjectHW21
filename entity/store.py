from entity.base_storage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def __str__(self):
        st = f'{self.__class__.__name__}:\n'

        for key, value in self._items.items():
            st += f"{key}: {value}\n"

        st += f'Свободно: {self.get_free_space()}\n'

        return st
