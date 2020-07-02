import telebot
import datetime
from componets.core import Hangman
bot = telebot.TeleBot('1287855639:AAE3Oe4FA19WGimahG_YbCVs8Zs4NIG2IHY')
# new_game_start = None


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, это игра Hangman. Введите команду /help для того чтобы получить информацию о других командах. Для того чтобы начать игру /game""")


@bot.message_handler(commands=['game'])
def game(message):
    global new_game_start
    new_game_start = Hangman()
    template = ' '.join(list(new_game_start.template))
    bot.send_message(message.chat.id, f"Бот загадал тебе слово длиной {new_game_start.word_lenght} символов. Попробуй угадать {template} и оно {new_game_start.word}")
 

@bot.message_handler(commands=['get_luck'])
def minigame(message):
    bot.send_message(message.chat.id, "Это специальная мини-игра, которая может помочь тебе выиграть, но также можно забрать у тебя одну жить. это мини-игра, кости. Бросаешь - побеждаешь, тут можно выбить один из трёх призов. Хочешь бросить?")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text_messages(message):
    msg = new_game_start.hangman_algorithm(str(message.text.lower()))
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)