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
        except InvalidRequest as error:
            print(f'Произошла ошибка: {error}')
            continue


if __name__ == '__main__':
    main()
