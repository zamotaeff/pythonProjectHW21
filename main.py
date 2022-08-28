from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items, capacity=100):
        self.__items = items
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    def add(self, title, quantity):
        pass

    def remove(self, title, quantity):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Shop(Store):
    def __init__(self, items, capacity=20):
        super(Shop, self).__init__(items, capacity)


class Request:
    def __init__(self, where_from, to, amount, product):
        self.where_from = where_from
        self.to = to
        self.amount = amount
        self.product = product
