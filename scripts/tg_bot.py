import telebot


class Bot:
    def __init__(self, token=""):
        self._bot = telebot.TeleBot(token)

    def send_message(self, destination, text):
        self._bot.send_message(destination, text)

    def start_polling(self):
        self._bot.polling(none_stop=True)


#def file_user_id(user, uid): # не вижу в этом необходимости, рома объяснит
#    # Открываем файл для записи
#    file = open(str(uid)+'.txt', 'w')
#    # Записываем
#    file.write("User: {}, id: {}\n".format(user, uid))
#    # Закрываем файл
#    file.close()

# @bot.message_handler(content_types=['text'])
# def send_message(message,text,id):
#
#     # bot = telebot.TeleBot("")
#     bot.send_message(id, text)
#     file_user_id(message.chat.id,)
#
#
# send_message(text="324234",id = someid)
#
# bot.polling(none_stop=True)







