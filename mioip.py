#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#Prova d'uso del modulo tanzocheck.py

from telegram import Updater
import logging
import telegram
import os
#Libreria per fare la richiesta http
import urllib.request

#Definisco le variabili globali
mioip=[]
numero1 = 0
numero2 = 0
operazione = []

#Definisco il metodo menu_keyboard per far apparire la tastiera
menu_keyboard = telegram.ReplyKeyboardMarkup([['*','+','-',':']])
menu_keyboard.one_time_keyboard=True
menu_keyboard.resize_keyboard=True
menu_keyboard.hide_keyboard=False

# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Definisco la funzione che viene chiamata quando arrivano dei messaggi
def messaggi_in_arrivo(bot, update):
	#Imposto l'uso delle variabili globali
	global mioip
	global numero1
	global numero2
	global operazione
	
	#Ciclo che imposta la variabile per controllare il processo
	if mioip==1: #se la variabile è 1 vuol dire che è stato immesso il primo valore quindi lo metto in memoria e chiedo di selezionare l'operazione e incremento la variabile
		numero1 = float(update.message.text)
		mioip=2
		bot.sendMessage(update.message.chat_id, "Scegli il tipo di operazione", reply_markup=menu_keyboard)
	if mioip==2: #se la variabile è 2 vuol dire che ho immesso l'operazione quindi vado a capire quale operazione è stata richiesta, imposto la nuova variabile di conseguenza e incremento la variabile di controllo di +1
		if update.message.text=="-":
			mioip=3
			operazione=0
			bot.sendMessage(update.message.chat_id, "hai chiesto la sottrazione!!")
		elif update.message.text=="+":
			mioip=3
			operazione=1
			bot.sendMessage(update.message.chat_id, "hai chiesto la somma!!")
		elif update.message.text=="*":
			mioip=3
			operazione=2
			bot.sendMessage(update.message.chat_id, "hai chiesto la moltiplicazione!!")
		elif update.message.text==":":
			mioip=3
			operazione=3
			bot.sendMessage(update.message.chat_id, "hai chiesto la divisione!!")
	if mioip==3:
		text = "Scrivi il secondo numero"
		bot.sendMessage(update.message.chat_id, text)
		mioip=4
	elif mioip==4:
		numero2 = float(update.message.text)
		mioip=0
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
# Definisco l'help
def comando_help(bot, update):
	help_text = (
	"Questi i comandi al momento disponibili:\n"
	"\n"
	"/mioip Scopri l'ip pubblico del tuo BOT!!\n"
	#"/userlist Lista utenti\n"
	#"/userdel Cancella tutti gli utenti\n"
	#"/info Informazioni utente\n"
	)
	bot.sendMessage(update.message.chat_id, help_text)
	
# Definisco la funzione di chiamata mioip
def comando_mioip(bot, update):
	my_ip = urllib.urlopen('http://ip.42.pl/raw').read()
	bot.sendMessage(update.message.chat_id, "L'IP publico del BOT è : " + my_ip)

KEY = os.environ['KEY_MisiBot']

updater = Updater(token=KEY)
dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(messaggi_in_arrivo)
dispatcher.addTelegramCommandHandler("help",comando_help)
dispatcher.addTelegramCommandHandler("mioip",comando_mioip)
updater.start_polling()
updater.idle()

