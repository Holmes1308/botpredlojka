import telebot
import constants
sms = 'Прислал '
bot = telebot.TeleBot(constants.token) #1
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет , присылай мне свои предложения и администратор рассмотрит их')
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_id = message.photo[-1].file_id
    bot.send_message(message.chat.id,'Ваше предложение отправлено на рассмотрение')
    bot.send_photo(constants.chat_id, file_id)#1
    bot.send_photo(284513694, file_id)
    if message.chat.username != None:                                       #ФОТО ЮЗЕРНЕЙМ
        bot.send_message(constants.chat_id,sms+'@'+message.chat.username+' через @cryptotime24_bot')#1
        bot.send_message(284513694,sms+'@'+message.chat.username+' через @cryptotime24_bot')
    else:                                                                    #ТЕКСТ ИМЯ
        bot.send_message(constants.chat_id,sms+message.chat.first_name+' '+message.chat.last_name+' через @cryptotime24_bot')#1
        bot.send_message(284513694,sms+message.chat.first_name+' '+message.chat.last_name+' через @cryptotime24_bot')
@bot.message_handler(content_types=['text'])
def handle_docs_text(message):
    sent = message.text
    bot.send_message(message.chat.id,'Ваше предложение отправлено на рассмотрение')
    bot.send_message(constants.chat_id, sent)#1
    bot.send_message(284513694, sent)
    if message.chat.username != None:                                       #ТЕКСТ ЮЗЕРНЕЙМ
        bot.send_message(constants.chat_id,sms+'@'+message.chat.username+' через @cryptotime24_bot')#1
        bot.send_message(284513694,sms+'@'+message.chat.username+' через @cryptotime24_bot')
    else:                                                                   #ТЕКСТ ИМЯ
        bot.send_message(constants.chat_id,sms+message.chat.first_name+' '+message.chat.last_name+' через @cryptotime24_bot')#1
        bot.send_message(284513694,sms+message.chat.first_name+' '+message.chat.last_name+' через @cryptotime24_bot')
bot.polling(none_stop=True)
bot.get_updates()
