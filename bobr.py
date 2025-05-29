import telebot
import random

TOKEN= '7903985712:AAEkwIWk86q4uYPXkT44ZuwXwBVywe4dUzM'
bot = telebot.TeleBot(TOKEN)
f = open('bobr', 'r', encoding='UTF-8')
bobr = f.read().split('\n')
f2 = open('los', 'r', encoding='UTF-8')
los = f2.read().split('\n')
f.close()
f2.close()

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Факт о Лосе', 'Факт о Бобре')
    markup.row('Фото Лося', 'Фото Бобра')
    bot.send_message(m.chat.id, 'Про какого животного хочешь узнать? Нажми: \nЛОСЬ, чтобы узнать факт о лосе \n\nБОБР, чтобы узнать факт о бобре', reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт о Лосе':
        answer = random.choice(los)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Фото Лося':
        bot.send_photo(message.chat.id, photo='https://upload.wikimedia.org/wikipedia/commons/4/47/Bigbullmoose.jpg')
    elif message.text.strip() == 'Факт о Бобре':
        answer = random.choice(bobr)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Фото Бобра':
        bot.send_photo(message.chat.id, photo='https://upload.wikimedia.org/wikipedia/commons/6/6b/American_Beaver.jpg')


if __name__ == '__main__':
    print("Бот запущен")
    bot.polling(none_stop=True)
