from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
from anketa import anketa_start, anketa_name, anketa_mail, anketa_skip
import logging

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуйте.При регистрации вы соглашаетесь с политикой конфидициальности(ссылка)',
    reply_markup=main_keyboard())


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Заполнить анкету'],
    ], resize_keyboard=True)


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

    dp.add_handler(anketa)
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()   
