class BaseError(Exception):
    message = 'Необработанная ошибка!'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос, попробуйте снова.'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места.'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара.'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много разных товаров.'


class ThereIsNoSuchWarehouse(BaseError):
    message = 'Такого склада нет.'
