import telebot

token = '497028477:AAERLo-AfA-NwqvcngZtuM5BvUq-wxVCLOM'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["text"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Ой, ну Привет...")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


if __name__ == '__main__':
    bot.polling(none_stop=True)
