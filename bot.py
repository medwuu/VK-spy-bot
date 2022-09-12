import config
import telebot
import parse

bot = telebot.TeleBot(config.TOKEN)
myID = config.ID

@bot.message_handler(commands=['start', 'help'])
def greeting(message):
    if message.chat.id == myID:
        bot.send_message(myID, "Привет, я бот, который поможет отседить статус человека во Вконтаке. Для начала пришли его никнейм. Например, напиши <u>id1</u>, чтобы искть vk.com/<u>id1</u>", parse_mode='html')
    else:
        bot.send_message(myID, f"Кто-то пытался воспользоваться вашим ботом!\n\n{message}")

@bot.message_handler(content_types=['text'])
def getNickname(message):
    if message.chat.id == myID:
        parse.main(message.text)
    else:
        bot.send_message(myID, f"Кто-то пытался воспользоваться вашим ботом!\n\n{message}")

def sendMessage(text):
    bot.send_message(myID, text, parse_mode='html')

bot.polling(non_stop=True)
