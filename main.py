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
    def items(self):
        return self.__items

    @property
    def capacity(self):
        return self.__capacity

    def add(self, title, quantity):
        if title in self.items.keys():
            if self.get_free_space() >= quantity:
                print("Товар добавлен")
                self.items[title] += quantity
                return True
            else:
                print("Недостаточно места на складе/магазине")
                return False
        else:
            if self.get_free_space() >= quantity:
                print("Товар добавлен")
                self.items[title] = quantity
                return True
            else:
                print("Недостатоно места на складе/магазине")
                return False

    def remove(self, title, quantity):
        if self.items[title] >= quantity:
            print("Такое количество товара на складе/в магазине есть")
            self.items[title] -= quantity
            return True
        else:
            print("Недостаточно места на складе/магазине")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.items.values():
            current_space += value
        return self.__capacity - current_space

    def get_unique_items_count(self):
        return len(self.items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.items.items():
            print(f"{key}:{value}")
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print("Cлишком много разных товаров")
            return False
        else:
            super().add(name, count)
            return True


class Request:
    def __init__(self, request_string):
        req_list = request_string.split(' ')
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        if self.__to == 'магазин':
            self.__to = 'shop'
        if self.__to == 'склад':
            self.__to = 'store'
        if self.__from == 'магазин':
            self.__from = 'shop'
        if self.__from == 'склад':
            self.__from = 'store'

        if eval(self.__from).remove(self.__product, self.__amount):
            eval(self.__to).add(self.__product, self.__amount)


store = Store(items={"печенька": 25, "собачка": 25, "елка": 25})
shop = Shop(items={"печенька": 2, "собачка": 2, "елка": 2})


def main():
    print('\nДобро пожаловать.\n')
    while True:
        print(f'Сейчас на складе:\n{store}')
        print(f'Сейчас в магазине:\n{shop}')
        user_input = input('Введите команду в формате "Доставить 1 собачка из склад в магазин"\n'
                           'Введите "стоп", если хотите закончить\n').lower()

        if user_input in ['стоп', 'stop']:
            print('До свидания')
            break

        try:
            request = Request(user_input)
            request.move()
        except Exception as e:
            print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    main()
