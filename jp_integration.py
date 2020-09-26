from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from business import second_keyboard

from web_api.backend.joinposter_api import JPApi


def anketa_start(update, context):
    update.message.reply_text(
        "Введите ФИО в формате - Иванов Иван Иваныч",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 3:
        update.message.reply_text("Пожалуйста введите Фамилию Имя Отчество")
        return "name"
    else:
        context.user_data["anketa"] = {"name": user_name}
        update.message.reply_text(
            "Введите дату рождения в формате - 25.05.1990"
        )
        return "mail"


def anketa_mail(update, context):
    user_birth = update.message.text
    context.user_data["anketa"]["birthday"] = user_birth
    update.message.reply_text(
        "Введите ваш email"
    )
    user_mail = update.message.text
    context.user_data["anketa"]["email"] = user_mail
    full_info = format_anketa(context.user_data['anketa'])
    #print(context.user_data)  
    return "full"


def format_anketa(anketa):
    full_info = {"name": anketa['name'], 
                 "birth": anketa['birthday'],
                 "email": anketa['email']  
                 }
    return full_info



def anketa_skip(update, context):
    update.message.reply_text('Регистрация завершена.', reply_markup=second_keyboard())
    return ConversationHandler.END
