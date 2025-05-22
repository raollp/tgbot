import telebot
import random

TOKEN= '7903985712:AAEkwIWk86q4uYPXkT44ZuwXwBVywe4dUzM'
bot = telebot.TeleBot(TOKEN)
i = 0
w = 0
@bot.message_handler(commands=['start'])
def send_welcome(mes):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Давай!', 'Не хочу!')
    bot.send_message(mes.chat.id, 'privet dawaj sygrajem w kamien noznicy bumagu\n\n/help - prawila igry\n/stat - statistika', reply_markup = markup)
@bot.message_handler(commands=['help'])
def send_welcome(mes):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Давай!', 'Не хочу!')
    bot.send_message(mes.chat.id, 'Победитель определяется по следующим правилам:\n\nБумага побеждает камень («бумага обёртывает камень»)\nКамень побеждает ножницы («камень затупляет ножницы»)\nНожницы побеждают бумагу («ножницы разрезают бумагу»)\n\ndawaj sygrajem', reply_markup = markup)
@bot.message_handler(commands=['stat'])
def send_welcome(mes):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Давай!', 'Не хочу!')
    bot.send_message(mes.chat.id,'kolichestwo pobed - '+str(w)+'\nkolichestwo sygranyh igr- '+str(i)+'\ndawaj sygrajem',reply_markup = markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global i
    global w
    if message.text.strip() == 'Давай!':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        k = telebot.types.KeyboardButton('Камень')
        markup.add(k)
        n = telebot.types.KeyboardButton('Ножницы')
        markup.add(n)
        b = telebot.types.KeyboardButton('Бумага')
        markup.add(b)
        bot.send_message(message.chat.id, 'Отлично! Делай свой выбор!', reply_markup=markup)
    elif message.text.strip() == 'Не хочу!':
        bot.send_message(message.chat.id, 'Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми Давай!', reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text.strip() == 'Камень':
        y = random.randrange(1,4)

        i += 1
        if y == 1:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id,'u nas nichya dawaj sygraem eshio',reply_markup=markup)
        elif y == 2:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ty wyigral dawaj sygraem eshio', reply_markup=markup)
            w +=1
        else:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ja wyigral dawaj sygraem eshio', reply_markup=markup)
    elif message.text.strip() == 'Ножницы':
        y = random.randrange(1,4)
        i+=1
        if y == 3:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id,'u nas nichya dawaj sygraem eshio',reply_markup=markup)
        elif y == 1:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ty wyigral dawaj sygraem eshio', reply_markup=markup)
            w+=1
        else:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ja wyigral dawaj sygraem eshio', reply_markup=markup)
    elif message.text.strip() == 'Бумага':
        y = random.randrange(1,4)
        i += 1
        if y == 2:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id,'u nas nichya dawaj sygraem eshio',reply_markup=markup)
        elif y == 1:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ty wyigral dawaj sygraem eshio', reply_markup=markup)
            w+=1
        else:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Давай!', 'Не хочу!')
            bot.send_message(message.chat.id, 'ja wyigral dawaj sygraem eshio', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'ne ponimaju tebia')


if __name__ == '__main__':
    print("Бот запущен")
    bot.polling(none_stop=True)