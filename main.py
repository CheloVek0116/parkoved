from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, 
                            CallbackQueryHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from anketa import anketa_start, anketa_name, anketa_mail, anketa_skip
from business import third_keyboard, pay_button
import logging

CALLBACK_BUTTON1_LEFT = "callback_button1_left"
TITLES = {CALLBACK_BUTTON1_LEFT: "ЕДА"}



logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуйте.При регистрации вы соглашаетесь с политикой конфидициальности(ссылка)',
    reply_markup=main_keyboard()) 


def menu(update, context):
    update.message.reply_text('Вот меню', reply_markup=inline_cafe_keyboard())
    

def menu_att(update, context):
    update.message.reply_text('Вот аттракционы', reply_markup=inline_attr_keyboard())


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Заполнить анкету'],
    ], resize_keyboard=True)


def cafe_choice(update, context):
    query = update.callback_query
    query.answer()
    data = query.data
    eat = "ЕДА"
    if data == CALLBACK_BUTTON1_LEFT:    
        query.edit_message_text(text=f"Вы выбрали: {eat}, напишите в чат - Оплатить.")


def inline_cafe_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
            InlineKeyboardButton('Напитки', callback_data='2')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def inline_attr_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Мероприятия', callback_data='1'),
            InlineKeyboardButton('Аттракцион', callback_data='2')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)        


def main():
    mybot = Updater('1308072242:AAE72OLIgP-150Rqlz-tjhPi6bNR0Hii3x0', use_context=True)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить анкету)$'), anketa_start)
        ],
        states={
            "name": [MessageHandler(Filters.text, anketa_name)],
            "mail": [MessageHandler(Filters.text, anketa_mail)],
            "full": [MessageHandler(Filters.text, anketa_skip)]
        },
        fallbacks=[]
    )


    dp.add_handler(CallbackQueryHandler(cafe_choice))
    dp.add_handler(MessageHandler(Filters.regex('^(Купить из кафе)$'), menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Купить билет на Аттракцион)$'), menu_att))
    dp.add_handler(MessageHandler(Filters.regex('^(Оплатить)'), pay_button))
    dp.add_handler(anketa)
    dp.add_handler(CommandHandler('start', greet_user))
    

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()   
