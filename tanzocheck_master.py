#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#Prova d'uso del modulo tanzocheck.py

from telegram import Updater
import logging
from tanzocheck import Check
import telegram

check=Check()

menu_keyboard = telegram.ReplyKeyboardMarkup([['/rele','/foto','/video','/logo','/start'],['/dog','/music','/jingle','/pdf','/graph'],['/mute','/menu']])
menu_keyboard.one_time_keyboard=False
menu_keyboard.resize_keyboard=True
menu_keyboard.hide_keyboard=True

# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.DEBUG)

logger = logging.getLogger(__name__)

def handle(msg):
    # questi sono i dati del messaggio in arrivo
    id_utente = msg['from']['id'] # id utente per rispondere male a chi non e' ablitato
    nome_utente = msg['from']['first_name'] # nome utente per rispondere con gentilezza ai comandi
    cognome_utente = msg['from']['last_name'] # cognome dell'utente che ha inviato il messaggio
    id_chat = msg['chat']['id'] # id della chat a cui rispondere
    testo = msg['text'].lower() # testo dei messaggi ricevuti, convertito tutto in minuscole per facilitare il lavoro con il parse
	

def messaggi_in_arrivo(bot, update):
	user_type= check.user(bot,update)
	
	if user_type=="none":
		bot.sendMessage(update.message.chat_id, "Accesso negato")
		return

	if user_type=="user":
		bot.sendMessage(update.message.chat_id, "User: [%s]" % update.message.from_user.username)
		return

	if user_type=="su":
		bot.sendMessage(update.message.chat_id, "Super user: [%s]" % update.message.from_user.username)
		return

def comando_start(bot, update):	
	user_type= check.user(bot,update)
	
	if user_type=="none":
		bot.sendMessage(update.message.chat_id, "Accesso negato")
		return

	if user_type=="user":
		bot.sendMessage(update.message.chat_id, "User: [%s]" % update.message.from_user.username)
		return

	if user_type=="su":
		bot.sendMessage(update.message.chat_id, "Super user: [%s]" % update.message.from_user.username)
		return

def comando_help(bot, update):
	help_text = (
	"/otp Genera una one time password\n"
	"/userlist Lista utenti\n"
	"/userdel Cancella tutti gli utenti\n"
	)
	user_type= check.user(bot,update)
	
	if user_type!="none":
		bot.sendMessage(update.message.chat_id, help_text)
		return

def comando_ciccio(bot, update):
	text = "Benvenuto username: %s\n" % update.message.from_user.username +  "Il tuo ID e': %s\n" % update.message.from_user.id + "Il messaggio che hai inviato e': %s\n" % update.message.text + 	" La chat e' di tipo: %s\n" % update.message.chat.type + "Il tuo message ID e' %s\n" % update.message.message_id +  "Il tuo Chat ID e' %s\n" % update.message.chat_id
	user_type= check.user(bot, update)
	#Nascondo la tastiera
	reply_markup = telegram.ReplyKeyboardHide()
	if user_type!="none":
		bot.sendMessage(update.message.chat_id, text, reply_markup=reply_markup)
		return

updater = Updater(token='')
dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(messaggi_in_arrivo)
dispatcher.addTelegramCommandHandler("start",comando_start)
dispatcher.addTelegramCommandHandler("help",comando_help)
dispatcher.addTelegramCommandHandler("ciccio",comando_ciccio)
check.addTanzoCheckCommandHandler(dispatcher)
updater.start_polling()
updater.idle()
