#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#Prova d'uso del modulo tanzocheck.py

from telegram.ext import Updater
import logging
from tanzocheck import Check
import telegram

check=Check()
calc=[]
numero1 = 0
numero2 = 0
operazione = []

menu_keyboard = telegram.ReplyKeyboardMarkup([['*','+','-',':']])
menu_keyboard.one_time_keyboard=True
menu_keyboard.resize_keyboard=True
menu_keyboard.hide_keyboard=False

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
	global calc
	global numero1
	global numero2
	global operazione
	user_type= check.user(bot,update)
	
	if user_type=="none":
		bot.sendMessage(update.message.chat_id, "Accesso negato")
		return

	if user_type=="user":
		if calc==1:
			numero1 = float(update.message.text)
			calc=2
			bot.sendMessage(update.message.chat_id, "Scegli il tipo di operazione", reply_markup=menu_keyboard)
		if calc==2:
			if update.message.text=="-":
				calc=3
				operazione=0
				bot.sendMessage(update.message.chat_id, "hai chiesto la sottrazione!!")
			elif update.message.text=="+":
				calc=3
				operazione=1
				bot.sendMessage(update.message.chat_id, "hai chiesto la somma!!")
			elif update.message.text=="*":
				calc=3
				operazione=2
				bot.sendMessage(update.message.chat_id, "hai chiesto la moltiplicazione!!")
			elif update.message.text==":":
				calc=3
				operazione=3
				bot.sendMessage(update.message.chat_id, "hai chiesto la divisione!!")
		if calc==3:
			text = "Scrivi il secondo numero"
			bot.sendMessage(update.message.chat_id, text)
			calc=4
			return
		elif calc==4:
			numero2 = float(update.message.text)
			calc=0
			if operazione==0:
				risultato = numero1 - numero2
			elif operazione==1:
				risultato = numero1 + numero2
			elif operazione==2:
				risultato = numero1 * numero2
			elif operazione==3:
				risultato = numero1 / numero2
			text = "Il risultato e':   %s" % risultato
			bot.sendMessage(update.message.chat_id, text)
			return
		elif update.message.text=="Ciao":
			bot.sendMessage(update.message.chat_id, "Super user: [%s]" % update.message.from_user.username)
		return

	if user_type=="su":
		if calc==1:
			numero1 = float(update.message.text)
			calc=2
			bot.sendMessage(update.message.chat_id, "Scegli il tipo di operazione", reply_markup=menu_keyboard)
		if calc==2:
			if update.message.text=="-":
				calc=3
				operazione=0
				bot.sendMessage(update.message.chat_id, "hai chiesto la sottrazione!!")
			elif update.message.text=="+":
				calc=3
				operazione=1
				bot.sendMessage(update.message.chat_id, "hai chiesto la somma!!")
			elif update.message.text=="*":
				calc=3
				operazione=2
				bot.sendMessage(update.message.chat_id, "hai chiesto la moltiplicazione!!")
			elif update.message.text==":":
				calc=3
				operazione=3
				bot.sendMessage(update.message.chat_id, "hai chiesto la divisione!!")
		if calc==3:
			text = "Scrivi il secondo numero"
			bot.sendMessage(update.message.chat_id, text)
			calc=4
			return
		elif calc==4:
			numero2 = float(update.message.text)
			calc=0
			if operazione==0:
				risultato = numero1 - numero2
			elif operazione==1:
				risultato = numero1 + numero2
			elif operazione==2:
				risultato = numero1 * numero2
			elif operazione==3:
				risultato = numero1 / numero2
			text = "Il risultato e':   %s" % risultato
			bot.sendMessage(update.message.chat_id, text)
			return
		elif update.message.text=="Ciao":
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
	"/info Informazioni utente\n"
	)
	user_type= check.user(bot,update)
	
	if user_type!="none":
		bot.sendMessage(update.message.chat_id, help_text)
		return

def comando_info(bot, update):
	
	# Modo 1 di mettere le variabili in un testo
	#text = "Benvenuto username: %s\n" % update.message.from_user.username +  "Il tuo first_name e': %s\n" % update.message.from_user.first_name + "Il tuo last_name e': %s\n" % update.message.from_user.last_name + "Il tuo user ID e': %s\n" % update.message.from_user.id + "Il messaggio che hai inviato e': %s\n" % update.message.text + 	"La chat e' di tipo: %s\n" % update.message.chat.type + "Il tuo message ID e' %s\n" % update.message.message_id +  "Il tuo Chat ID e' %s\n" % update.message.chat_id
	
	# Modo 2 di mettere le variabili in un testo
	text = "Benvenuto username: %s\nIl tuo first_name e': %s\nIl tuo last_name e': %s\nIl tuo user ID e': %s\nIl messaggio che hai inviato e': %s\nLa chat e' di tipo: %s\nIl tuo message ID e' %s\nIl tuo Chat ID e' %s\n" % (update.message.from_user.username, update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.id, update.message.text, update.message.chat.type, update.message.message_id, update.message.chat_id)
	user_type= check.user(bot, update)
	
	#Nascondo la tastiera
	#nascondi_tastiera = telegram.ReplyKeyboardHide()
	#menu_keyboard = telegram.ReplyKeyboardMarkup([['/rele','/foto','/video','/logo','/start'],['/dog','/music','/jingle','/pdf','/graph'],['/mute','/menu']])
	#risposta_obbligatoria = telegram.ForceReplay()
	if user_type!="none":
		bot.sendMessage(update.message.chat_id, text)
		return

def comando_calc(bot, update):
	global calc
	user_type = check.user(bot, update)
	if user_type!="none":
		calc = 1
		text= "Inserisci il primo numero"
		bot.sendMessage(update.message.chat_id, text)
		return


updater = Updater(token='')
dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(messaggi_in_arrivo)
dispatcher.addTelegramCommandHandler("start",comando_start)
dispatcher.addTelegramCommandHandler("help",comando_help)
dispatcher.addTelegramCommandHandler("info",comando_info)
dispatcher.addTelegramCommandHandler("calc",comando_calc)
check.addTanzoCheckCommandHandler(dispatcher)
updater.start_polling()
updater.idle()
