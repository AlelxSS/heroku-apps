import telebot
import random

token = '497028477:AAERLo-AfA-NwqvcngZtuM5BvUq-wxVCLOM'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def answer_all_messages(message): 
	if (message.text.lower().find('привет')>=0) or (message.text.lower().find('здаров')>=0): 
		foo1 = ['И тебе привет', 'Аггаа', 'Ой, ну привеет...']
		bot.send_message(message.chat.id, random.choice(foo1))
	elif (message.text.lower().find('почему')>=0): 
		foo2 = ['Потому', 'Потому что', 'Покочену!']
		bot.send_message(message.chat.id, random.choice(foo2))
	elif (message.text.lower().find('зачем')>=0): 
		foo3 = ['А вот затем', 'Надо', 'За шкафом']
		bot.send_message(message.chat.id, random.choice(foo3))
	elif (message.text.lower().find('что')>=0): 
		foo4 = ['Что-то', '...', 'Ой ну все']
		bot.send_message(message.chat.id, random.choice(foo4))
	elif (message.text.lower().find('кто')>=0): 
		foo5 = ['Кто-то', 'Кто-то', '...']
		bot.send_message(message.chat.id, random.choice(foo5))
	elif (message.text.lower().find('кого')>=0): 
		foo6 = ['Кого-то', 'Кого-то', 'Аййй..']
		bot.send_message(message.chat.id, random.choice(foo6))
	elif (message.text.lower().find('как ')>=0): 
		foo7 = ['Как-то', 'Каком к верху', 'Отстань!']
		bot.send_message(message.chat.id, random.choice(foo7))
	elif (message.text.lower().find('кому')>=0): 
		foo8 = ['Кому-то']
		bot.send_message(message.chat.id, random.choice(foo8))
	elif (message.text.lower().find('когда')>=0): 
		foo9 = ['Не знаю', '...']
		bot.send_message(message.chat.id, random.choice(foo9))
	elif (message.text.lower().find('какой')>=0): 
		foo10 = ['Какой-то']
		bot.send_message(message.chat.id, random.choice(foo10))
	elif (message.text.lower().find('куда')>=0): 
		foo11 = ['Куда-то']
		bot.send_message(message.chat.id, random.choice(foo11))
	elif (message.text.lower().find('чей')>=0): 
		foo12 = ['Общий']
		bot.send_message(message.chat.id, random.choice(foo12))
	elif (message.text.lower().find('где')>=0): 
		foo13 = ['Где-то', 'В караганде', 'Аййй..']
		bot.send_message(message.chat.id, random.choice(foo13))
	else:
		foo14 = ['Ой все', 'Отстань', 'Ай', '...']
		bot.send_message(message.chat.id, random.choice(foo14))
	
	

if __name__ == '__main__':
    bot.polling(none_stop=True)
