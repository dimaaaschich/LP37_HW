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
import logging, ephem, settings
from datetime import * # модуль для определения сегодняшней даты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log') # куда пишутся события

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Для того чтобы узнать в каком созвездии сегодня находится '
                              'планета ведите её название по английски после команды /planet '
                              '(например /planet mars)')

def enter_planet(update, context):
    planets_list = ['Jupiter', 'Mars', 'Mercury', 'Moon', 'Neptune', 'Saturn', 'Uranus', 'Venus']
    pl_name = (update.message.text.split()[1]).lower().capitalize()
    #print(pl_name)
    if pl_name in planets_list:
        planet = ephem.constellation(getattr(ephem, pl_name)(datetime.today()))
        update.message.reply_text(planet[1])
    else:
        update.message.reply_text('Нет такой планеты')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", enter_planet))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
