from typing import Dict

from exceptions import ThereIsNoSuchWarehouse

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.destination not in storages or self.__request.departure not in storages:
            raise ThereIsNoSuchWarehouse

        self.destination = storages[self.__request.destination]
        self.departure = storages[self.__request.departure]

    def move(self):
        self.departure.remove(
            title=self.__request.title,
            quantity=self.__request.quantity
        )

        print(f'Курьер забрал {self.__request.quantity} {self.__request.title} из {self.__request.departure}')

        self.destination.add(
            title=self.__request.title,
            quantity=self.__request.quantity
        )

        print(f'Курьер Доставил {self.__request.quantity} {self.__request.title} в {self.__request.destination}')

    def cancel(self):
        pass
