from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
