import telebot

token = '497028477:AAERLo-AfA-NwqvcngZtuM5BvUq-wxVCLOM'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Ой, ну Привеет...")

@bot.message_handler(content_types=["text"])
def answer_all_messages(message): 
	if(message.text.lower.find('привет')): 
	bot.send_message(message.chat.id, 'И тебе привет')
	return

if __name__ == '__main__':
    bot.polling(none_stop=True)
