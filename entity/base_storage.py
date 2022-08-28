from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, title: str, quantity: int) -> None:

        if self.get_free_space() < quantity:
            raise NotEnoughSpace

        if title in self._items:
            self._items[title] += quantity
        else:
            self._items[title] = quantity

    def remove(self, title: str, quantity: int) -> None:
        if title not in self._items or self._items[title] < quantity:
            raise NotEnoughProduct

        self._items[title] -= quantity

        if not self._items[title]:
            self._items.pop(title)

    def get_free_space(self) -> int:
        current_space = 0

        for value in self._items.values():
            current_space += value

        return self._capacity - current_space

    def get_items(self) -> Dict[str, int]:
        return self._items

    def get_unique_items_count(self):
        return len(self._items.keys())
