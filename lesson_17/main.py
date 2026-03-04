import telebot
from model import *

bot = telebot.TeleBot('8303579544:AAE-D-LxtSOfVeWC7dLena4wwphzCuBVpaQ')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Я умею:
    /hello - Приветствие
    /travel - рассказ о приключениях
    /weather - Что я думаю о погоде
    /online - В сети
    /telegram - Телеграм
    /me - Информация о тебе
    /forchan - Форчан
    /photo - Фото
    /bye - бот прошается с вами
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['travel'])
def send_travel(message):
    bot.reply_to(message, "Я считаю что путешествия это важно!")

@bot.message_handler(commands=['me'])
def send_me(message):
    bot.reply_to(message, "Не знаю что вы имеете в виду. Но я вас уважаю как человека.")

@bot.message_handler(commands=['online'])
def send_online(message):
    bot.reply_to(message, "Да я сейчас и всегда нахожусь в сети.")

@bot.message_handler(commands=['weather'])
def send_weather(message):
    bot.reply_to(message, "Я думаю вам нравиться говорить о погод. Извините, я ещё не могу смотреть погоду.")

@bot.message_handler(commands=['telegram'])
def send_telegram(message):
    bot.reply_to(message, "Телеграм это соцсеть созданная Павлом и Николаем Дуровым")

@bot.message_handler(commands=['forchan'])
def send_forchan(message):
        bot.reply_to(message, "Форчан это соцсеть не известно кем созданная но там проварачивают дела мирового уровня.")

@bot.message_handler(content_types=['photo'])
def send_getphoto(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result=get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name)
    bot.reply_to(message, result)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()