import telebot
import random

token = '497028477:AAERLo-AfA-NwqvcngZtuM5BvUq-wxVCLOM'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def answer_all_messages(message): 
	if (message.text.lower().find('привет')>=0) or (message.text.lower().find('здаров')>=0): 
		foo1 = ['И тебе привет', 'Аггаа', 'Ой, ну привеет...']
		bot.send_message(message.chat.id, random.choice(foo1))

if __name__ == '__main__':
    bot.polling(none_stop=True)
