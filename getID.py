import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def getID(message):
    bot.send_message(message.chat.id, f"Ваш ID: <code>{message.chat.id}</code>", parse_mode='html')

bot.polling(non_stop=True)