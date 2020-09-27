from telegram import ReplyKeyboardMarkup


def second_keyboard():
    return ReplyKeyboardMarkup([
        ['Купить из кафе'], ['Купить билет на Аттракцион'],
    ], resize_keyboard=True)


def third_keyboard():
    return ReplyKeyboardMarkup([
        ['Оплата']
    ], resize_keyboard=True)


def pay_button(update, context):
    pay_tm = update.message.text
    if pay_tm == 'Оплатить':
        update.message.reply_text("https://oplata.qiwi.com/form?invoiceUid=0a28446a-4d57-4a5b-9330-e4ee9205f2e3")


               


    


    