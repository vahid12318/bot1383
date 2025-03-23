import telebot

API_TOKEN = "8136878149:AAFN_Cx8WhCX21HVJ3aCNzj0xgBLfBovQdA"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'welcome to nani')



bot.polling()