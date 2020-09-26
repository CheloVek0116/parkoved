from telegram import ReplyKeyboardMarkup


def second_keyboard():
    return ReplyKeyboardMarkup([
        ['Купить из кафе'], ['Купить билет на Аттракцион'],
    ], resize_keyboard=True)

