import telepot
import sys
import time
import datetime
import os
from pprint import pprint

def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        
        if content_type != 'text':
            bot.sendMessage(chat_id, "Per ora scrivimi solo messaggi di testo, non siamo ancora cosi in confidenza...")
        cmd = msg['text']

        if cmd == '/lol' or cmd == '/Lol' or cmd == '/LOL':
            bot.sendMessage(chat_id, "Onesto!")
        elif cmd == '/start':
            bot.sendMessage(chat_id, "Ciao, si, sono felice anche io di sentirti, lo so che non vedi l'ora, grazie")
            bot.sendMessage(chat_id, "Lista comandi:")
            bot.sendMessage(chat_id, "/Lol    /Onesto    /Time    /Righini    /Help")
            bot.sendMessage(chat_id, "Digita /Help per la lista dei comandi disponibili")
        elif cmd == '/Onesto' or cmd == '/onesto' or cmd == '/ONESTO':
            bot.sendMessage(chat_id, "LOL!")
        elif cmd == '/time' or cmd == '/Time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif cmd == '/righini' or cmd == '/Righini':
            bot.sendAudio(chat_id, audio=open('migliore.mp3', 'rb'))
        elif cmd == '/Limardo' or cmd == '/limardo':
            bot.sendMessage(chat_id, "Ma perche tu mi in***li tutte le volte?!")
        elif cmd == '/TiTrollo' or cmd == '/Titrollo':
            bot.sendMessage(chat_id, "Ma tu lo sai che in pratica sto distruggendo la tua privacy loggando ogni messaggio che mi scrivi con tutte le info possibili all'idiota che mi ha creato?? Non so quanto sia legale ma che rimanga tra di noi ;)")
        elif cmd == '/Help' or cmd == '/help':
            #help()
            bot.sendMessage(chat_id, "Lista comandi:")
            bot.sendMessage(chat_id, "/Lol    /Onesto    /Time    /Righini    /Help")
        else:
            bot.sendMessage(chat_id, "Devi scrivermi un comando, non cose a caso...")
            #help()
            bot.sendMessage(chat_id, "Lista comandi:")
            bot.sendMessage(chat_id, "/Lol    /Onesto    /Time    /Righini    /Help")
            bot.sendMessage(chat_id, "Digita /Help per la lista dei comandi disponibili")

        updts = bot.getUpdates()
        pprint(updts)
#
#def help():
#        bot.sendMessage(chat_id, "Lista comandi:")
#        bot.sendMessage(chat_id, "/Lol    /Onesto    /Time    /Righini    /Help")

bot = telepot.Bot(os.environ["TELEGRAM_TOKEN"])
bot.message_loop(handle)

while 1:
	time.sleep(10)

	

