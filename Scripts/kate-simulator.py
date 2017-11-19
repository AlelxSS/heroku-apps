import telebot

token = '497028477:AAERLo-AfA-NwqvcngZtuM5BvUq-wxVCLOM'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def answer_all_messages(message): 
	if message.text.lower.find('привет')>=0: 
		bot.send_message(message.chat.id, 'И тебе привет')

if __name__ == '__main__':
    bot.polling(none_stop=True)
