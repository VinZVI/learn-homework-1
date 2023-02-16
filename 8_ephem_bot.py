"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_constellation(update, context):
    user_text = update.message.text
    name_planet = user_text.split()[1].lower()


    planet_dict = {
        'jupiter': ephem.Jupiter(),
        'saturn': ephem.Saturn(),
        'uranus': ephem.Uranus(),
        'neptune': ephem.Neptune(),
        'mars': ephem.Mars(),
        'venus': ephem.Venus(),
        'moon': ephem.Moon(),
        'mercury': ephem.Mercury(),
        'pluto': ephem.Pluto()
    }
    class_planet = planet_dict.get(name_planet)
    if class_planet:

        today = datetime.date.today()
        class_planet.compute(today)

        constellation_name = ephem.constellation(class_planet)

        update.message.reply_text(f'"{name_planet.capitalize()}" cегодня находится в созвездии "{constellation_name[1]}"')

    else:
        update.message.reply_text(f'Планета "{name_planet.capitalize()}" не найдена, попробуйте еще раз.')

def main():
    mybot = Updater(settings.TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
