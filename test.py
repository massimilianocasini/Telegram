 from telegram import Updater

updater = Updater(token='138682670:AAGpVS2brpdVCpJ872ZGl5sbe9KQbFUjAZQ')
dispatcher = updater.dispatcher
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
dispatcher.addTelegramCommandHandler('start', start)
updater.start_polling()
updater.idle()