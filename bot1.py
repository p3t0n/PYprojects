# -*- coding: utf-8 -*-

import config
import telebot
import random


bot=telebot.TeleBot(config.token)


"""генерируем случайный ответ"""
randomize=['определенно!', 'никак нет!', 'обратись с этим вопросом к богу..', 'это не в моей власти..']
know=random.choice(randomize)


"""Функция приветствия"""
@bot.message_handler(commands=['start'])
def start(message):
    sent=bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть!'.format(name=message.text))


"""получение информации о боте"""
@bot.message_handler(commands=['info'])
def inform(message):
    bot.send_message(message.chat.id, 'Это первая версия бота Виктория. Доступные фукнции можно узнать с помощью: !functions. Ждите обновлений!')


"""Фунция предсказания"""
@bot.message_handler(commands=['predict'])
def prediction_1(message):
    sent=bot.send_message(message.chat.id, 'Задай мне вопрос, и я дам тебе ответ..')
    bot.register_next_step_handler(sent, prediction_2)
    
def prediction_2(message):
    know=random.choice(randomize)
    mes='Мой ответ: '+str(know)
    bot.send_message(message.chat.id, mes)
    

bot.polling()
