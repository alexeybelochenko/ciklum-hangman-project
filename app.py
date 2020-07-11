import telebot
from telebot import types
import datetime
from components.core import Hangman, Minigame

bot = telebot.TeleBot('1287855639:AAE3Oe4FA19WGimahG_YbCVs8Zs4NIG2IHY')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, это игра Hangman. Для того чтобы начать игру /game""")

@bot.message_handler(commands=['tips'])
def tips(message):
    try:
        tip = new_game_start.tips() 
        bot.send_message(message.chat.id, f"Подсказка: {tip}")
    except:
        bot.send_message(message.chat.id, 'Для начала начните игру /game')

@bot.message_handler(commands=['game'])
def game(message):
    global new_game_start
    new_game_start = Hangman()
    template = ' '.join(list(new_game_start.template))
    bot.send_message(message.chat.id, f"Бот загадал тебе слово длиной {new_game_start.word_lenght} символов. Попробуй угадать {template}.")
 

@bot.message_handler(func=lambda message: message.text[0] != '/', content_types=['text'])
def handle_text_messages(message):
    try:
        msg = new_game_start.hangman_algorithm(str(message.text.lower()))
        bot.send_message(message.chat.id, msg)
    except:
        bot.send_message(message.chat.id, 'Для начала начните игру /game')

@bot.message_handler(commands=['get_luck'])
def minigame(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Эх, погнали', callback_data='yes')
    button2 = telebot.types.InlineKeyboardButton(text='Нет, давай в другой раз', callback_data='no')
    markup.add(button1, button2)
    try:
        if new_game_start:
            bot.send_message(message.chat.id, "Это специальная мини-игра, которая может помочь тебе выиграть, но также может забрать у тебя одну жизнь. Это мини-игра - кости. Бросаешь - побеждаешь, тут можно выбить один из трёх призов. Хочешь бросить?", reply_markup=markup)
    except:
        bot.send_message(message.chat.id, "Для начала нужно начать игру :sun_with_face:, а потом кидать кости")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'yes':
        mn = Minigame()
        result = mn.throw()
        bot.answer_callback_query(callback_query_id=call.id, text=result)
    elif call.data == 'no':
        mn.foo()
        bot.answer_callback_query(callback_query_id=call.id, text='В другой раз, но я вынужден забрать у тебя одну возможность')
    

bot.polling(none_stop=True, interval=0)