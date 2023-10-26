from random import choice
from glob import glob
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

TOKEN = '6387838921:AAHY4J_099TAiCxLRBicdAGdflnrKvjunbM'

def start(update, context):
    update.message.reply_text("PROVAAAAAAAAAA")

def rispondi(update, context):
    testo_messaggio = update.message.text.lower()
    if testo_messaggio == "dove sei?":
        update.message.reply_venue(43.08234991198937, 12.270208667524441, "Solomeo", "Casa mia")
    elif "matteo" in testo_messaggio:
        update.message.reply_contact("Il suo numero di telefono è 3404013218")
    elif "foto" in testo_messaggio:
        immagine = choice(glob("foto/Immagine.png"))
        update.message.reply_photo(open(immagine, 'rb')) # rb sta per lettura binaria
    elif "video" in testo_messaggio:
        update.message.reply_video(open("dolce_gattino.mp4", 'rb')) # rb sta per lettura binaria
    else:
        update.message.reply_text("scrivimi qualcosa di sensato")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(filters.text, rispondi))
print("bot in ascolto...")
updater.start_polling()

#https://www.youtube.com/watch?v=lXJ65f2vPTE