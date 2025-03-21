import telebot, time
from botlogic import passgen
from config import token  
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands = ["generate_password"])  
def password_maker(message):
    args = message.text.split()
    if len(args) != 2 :
        bot.send_message(message.chat.id, "используйте /generate_password и длина пароля")
        return
    dlina = int(args[1])
    if dlina < 3:
        bot.send_message(message.chat.id, "длина пароля должна быть больше трех")
        return
    bot.send_message(message.chat.id, passgen(dlina))
    
    






bot.polling()