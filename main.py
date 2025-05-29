import telebot
import random

TOKEN= '7903985712:AAEkwIWk86q4uYPXkT44ZuwXwBVywe4dUzM'
bot = telebot.TeleBot(TOKEN)

da = ['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть','da']
net = ['Нет', 'Не', 'Не хочу', 'Не буду','net']
user = {'in_game': False, 'secret_number': None, 'attempts': 5, 'total_games': 0, 'wins': 0, 'in_set':False}

def get_random_number():
    return random.randint(1, 100)
@bot.message_handler(commands=['start'])
def send_welcome(mes):
    msg = bot.send_message(mes.chat.id, 'Привет!\nДавай сыграем в игру "Угадай число"?\n\nЧтобы получить правила игры и список доступных команд - отправьте команду /help')
@bot.message_handler(commands=['stas'])
def stas(message):
    bot.reply_to(message, "stas loh")
@bot.message_handler(commands=['maxim'])
def maxim(message):
    bot.reply_to(message, "maxim molodec")
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Правила игры:\n\nЯ загадываю число от 1 до 100, а вам нужно его угадать\nУ вас есть 5 попыток\n\nДоступные команды:\n/help - правила игры и список команд\n/cancel - выйти из игры\n/stat - посмотреть статистику\n/set - zadat kolichestwo popytok\n\nДавай сыграем?')
@bot.message_handler(commands=['cancel'])
def cancel(message):
    if user['in_game']:
        bot.send_message(message.chat.id, 'Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
        user['in_game'] = False
    else:
        bot.send_message(message.chat.id, 'А мы итак с вами не играем. Может, сыграем разок?')
@bot.message_handler(commands=['stat'])
def stat(messege):
    bot.send_message(messege.chat.id, 'Всего игр сыграно: ' + str(user["total_games"]) + '\nИгр выиграно: ' + str(user["wins"]))
@bot.message_handler(commands=['set'])
def stat(messege):
    bot.send_message(messege.chat.id, 'napishi kolichestwo popytok')
    user['in_set'] = True
@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        chislo = int(message.text)
        if user['in_game']:
            if chislo == user['secret_number']:
                bot.send_message(message.chat.id, 'Ypa!!! Вы угадали число!\n\nМожет, сыграем еще?')
                user['in_game'] = False
                user['total_games'] += 1
                user['wins'] += 1
            elif chislo > user['secret_number']:
                bot.send_message(message.chat.id, 'Мое число меньше')
                user['attempts'] -= 1
            elif chislo < user['secret_number']:
                bot.send_message(message.chat.id, 'Мое число больше')
                user['attempts'] -= 1
            if user['attempts'] == 0:
                bot.send_message(message.chat.id, 'К сожалению, у вас больше не осталось попыток. Вы проиграли :(\n\n' 'Мое число было ' + str(user['secret_number']) + '\n\nДавайте сыграем еще?')
                user['in_game'] = False
                user['total_games'] += 1
        elif user['in_set']:
            user['attempts'] = chislo
            bot.send_message(message.chat.id, 'wy zadali kolichestwo popytok, dawajte sygrajem? ')
            user['in_set']= False
        else:
            bot.send_message(message.chat.id, 'Мы еще не играем. Хотите сыграть?')
    except Exception:
        if message.text in da:
            if not user['in_game']:
                bot.send_message(message.chat.id, 'Ура!\n\nЯ загадал число от 1 до 100, попробуй угадать!')
                user['in_game'] = True
                user['secret_number'] = get_random_number()

        elif message.text in net:
            if not user['in_game']:
                bot.send_message(message.chat.id, 'Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
            else:
                bot.send_message(message.chat.id, 'Мы же сейчас с вами играем. Присылайте, пожалуйста, ''числа от 1 до 100')
        elif user['in_set']== True:
            bot.send_message(message.chat.id, 'my sejchas zadajem kolichistwo popytok, napishite pozalujsta chislo')
        elif user['in_game']==True:
            bot.send_message(message.chat.id, 'Пока мы играем в игру я могу реагировать только на: ''\n- числа от 1 до 100 \n- команды /cancel и /stat')


