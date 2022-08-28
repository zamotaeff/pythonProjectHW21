from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import InvalidRequest

store = Store(items={"печенька": 25, "собачка": 25, "елка": 25})
shop = Shop(items={"печенька": 2, "собачка": 2, "елка": 2})

storages = {
    'магазин': shop,
    'склад': store
}


def main():

    print('\nДобро пожаловать.\n')

    while True:

        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}\n')

        user_input = input('Введите команду в формате "Доставить 1 собачка из склад в магазин"\n'
                           'Введите "стоп", если хотите закончить\n').lower()

        if user_input in ['стоп', 'stop']:
            print('До свидания')
            break

        try:
            request = Request(user_input)
        except InvalidRequest as error:
            print(f'Произошла ошибка: {error}')
            continue

        courier = Courier(
            request,
            storages
        )

        courier.move()


if __name__ == '__main__':
    main()
