import math

import telebot
from telebot import types

import config

bot = telebot.TeleBot(token=config.token)


@bot.message_handler(commands=["start"])
def start(message):
    # print(message)
    if message.from_user.first_name == None:
        message.from_user.first_name = 'друг'
    mess = f'Привет, {message.from_user.first_name}!'
    mess1 = 'Меня зовут Настя и я 3D-визуализатор интерьеров.\n' \
            'Этот чат-бот поможет вам рассчитать стоимость визуализации вашего интерьера.'
    markup = types.InlineKeyboardMarkup(row_width=2)
    url = types.InlineKeyboardButton('Ознакомиться с моим портфолио',
                                     url='https://www.behance.net/khanetskaya')
    callback = types.InlineKeyboardButton('Рассчитать стоимость визуализации',
                                          callback_data='call_to_price')
    markup.add(url, callback)
    bot.send_message(message.chat.id, f'{mess}\n{mess1}', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data_1(callback):
    text_price = ' Расчёт стоимости производится в зависимости от квадратных метров\n'
    text_veriant = '\nВыберите нужную вам квадратуру в <b>м&#178</b> :'
    text1 = 'до 10'
    text2 = 'от 10 до 150'
    # text3 = 'от 150'
    if callback.data == 'call_to_price':
        markup1 = types.InlineKeyboardMarkup(row_width=3)
        bt1 = types.InlineKeyboardButton(text=text1, callback_data='btn1')
        bt2 = types.InlineKeyboardButton(text=text2, callback_data='btn2')
        # bt3 = types.InlineKeyboardButton(text=text3, callback_data='btn3')
        markup1.add(bt1, bt2)
        bot.send_message(callback.message.chat.id,
                         f'{text_price}{text_veriant}',
                         reply_markup=markup1,
                         parse_mode='html')
    if callback.data == 'btn1':
        text1 = 'Стоимость вашей визуализации будет 100$'
        bot.send_message(callback.message.chat.id, f'{text1}', parse_mode='html')
    if callback.data == 'btn2':
        text4 = 'Для расчета стоимости введите количество квадратных метров'
        bot.send_message(callback.message.chat.id, f'{text4}', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    text = message.text.replace(",", ".").replace(" ", "")
    try:
        text = float(text)
        if 10 < text < 150:
            result = text * 7
            bot.send_message(message.chat.id,
                             f'Общаяя стоимость  <b>{round(result)}$</b> ',
                             parse_mode='html')
        elif text > 150:
            result = text * 6
            bot.send_message(message.chat.id,
                             f'Общаяя стоимость  <b>{math.ceil(result)}$</b>',
                             parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'Введите данные в формате ХХ,Х или ХХ.Х', parse_mode='html')
    except:
        bot.send_message(message.chat.id, f'Введите данные в формате ХХ,Х или ХХ.Х', parse_mode='html')


bot.polling(none_stop=True, interval=0)

# if isinstance(text, float):
#     # bot.send_message(message.chat.id, message, parse_mode='html')
#     bot.send_message(message.chat.id, 'И тебе привет! вот ссылка '
#                                       '<a href="https://telegram.com/Nastya">instargamm Nastya</a>',
#                      parse_mode='html')
# elif message.text == 'id':
#     bot.send_message(message.chat.id, f'You ID:{message.for_user.id}', parse_mode='html')
# elif message.text == 'photo':
#     photo = open('korm.jpeg', 'rb')
#     bot.send_photo(message.chat.id, photo)
# else:
#     bot.send_message(message.chat.id, f'I`am no understand you', parse_mode='html')


#
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data_2(callback):
#     print(callback)
#     print(callback.data)
#     if callback.data == 'btn1':
#         text1 = 'Стоимость вашей визуализации будет 100$'
#         bot.send_message(callback.message.chat.id, f'{text1}', parse_mode='html')
#     if callback.data == 'btn2':
#         @bot.message_handler(content_types=['text'])
#         def check_message1(message):
#             print(message)
#
#         text2 = 'Для расчета стоимости введите количество квадратных метров'
#         bot.send_message(callback.message.chat.id, f'{text2}', parse_mode='html')
#

#
# @bot.message_handler()  # content_types=['text'] какой тип данных принимать
# def get_user_text(message):
#     if message.text == 'Hello':
#         # bot.send_message(message.chat.id, message, parse_mode='html')
#         bot.send_message(message.chat.id, 'И тебе привет! вот ссылка '
#                                           '<a href="https://telegram.com/Nastya">instargamm Nastya</a>',
#                          parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'You ID:{message.for_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('korm.jpeg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, f'I`am no understand you', parse_mode='html')

#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'cool')
#
#
# # button
# @bot.message_handler(commands=['website'])
# def website(message):  # метод который выводитт нам кнопки
#     markup = types.InlineKeyboardMarkup()  # встроеные в сообщения кнопки, изображения и другое(ссылка под сообщнием)
#     markup.add(types.InlineKeyboardButton('enter sie', url="www.google.com"))
#     bot.send_message(message.chat.id, 'to site', reply_markup=markup)  # reply_markup=markup (вывод нашей кнопки)
#
#
# @bot.message_handler(commands=['help'])
# def website(message):  # метод который выводитт нам кнопки
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
#                                        row_width=2)  # кнопки в поле для ввода, resize_keyboard=True чтоб было как на телефоне так и на компе(будт подстраиваться под нужный размер), row_width=2 (количество кнопок в ширину)
#     website = types.KeyboardButton('website')
#     start = types.KeyboardButton('/start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'to site', reply_markup=markup)
#
#
# bot.polling(none_stop=True, interval=0)  # запустить бота на постоянку
