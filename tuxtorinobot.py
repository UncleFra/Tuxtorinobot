#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import logging
import html

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Token
TOKEN = '<Your token>'

# Messages
ASSISTANCE = '<b>Sportello OIL</b>\n\nLo sportello di assistenza linux è attivo dalle <b>18</b>\
 alle <b>19:30</b> di <b>mercoledì</b>\nPer info e prenotazioni scrivere a \
<b><i>bob@linux.it</i></b>\n<i>È chiuso nel mese di agosto e nel \
periodo natalizio. Potrebbe essere annullato, molto raramente, in caso di \
 assenza prenotazioni</i>\n\nPosizione:\nOpenStreetMap - https://www.openstreetmap.org/node/7125752145\
\nGoogle Maps https://goo.gl/maps/VmHujy9UY8mkqNEj8\n\nLink utili\nhttps://torino.ils.org/'

START = 'Bot per il gruppo linux torino https://t.me/linuxtorino'

LINUX_ADVANCED = '<b>Corso GNU/Linux avanzato e tecnologie aperte</b>\n\nCorso avanzato dove vengono illustrati\
 alcuni tools più avanzati per la gestione di sistemi linux.\n\n<i>L\'edizione del prossimo anno verrà organizzata\
 nella primavera 2023, in attesa della prossima edizione è possibile recuperare le registrazioni degli anni\
 precedenti</i>\n\nPosizione:\nOpenStreetMap - https://www.openstreetmap.org/node/7125752145\nGoogle Maps\
 https://goo.gl/maps/VmHujy9UY8mkqNEj8\n\nLink utili\nRegistrazioni degli anni precedenti - \
https://linux.studenti.polito.it/wp/video-corso-gnu-linux-avanzato-e-tecnologie-aperte/\nCanale telegram - https://t.me/corsolinuxpolito'

LINUX_BASIC = '<b>Corso GNU/Linux base</b>\n\nCorso base dove si imparano i fondamentali di un sistema liunx attraverso \
 l\'utilizzo del terminale.\n\nOrario: <b>19</b> - <b>20:30</b>\n\n<b>Lezioni anno 2022:</b>\n💠 Lezione 1 -\
 25/10/2022\n💠 Lezione 2 - 08/11/2022\n💠 Lezione 3 - 15/11/2022\n💠 Lezione 4 - 22/11/2022\n💠 Lezione 5 -\
 29/11/2022\n💠 Lezione 6 - 06/12/2022\n💠 Lezione 7 - 13/12/2022\n💠 Lezione 8 - 20/12/2022\n\n<i>Sarà possibile\
 ricevere assistenza personalizzata per eventuali problematiche un\'ora prima della lezione (<b>18</b> - <b>19</b>)\
 in <b>aula 5</b></i>\n\nPosizione: \nPolitecnico di Torino (Aula 5)\nOpenStreetMap - https://www.openstreetmap.org/relation/3802268\n\
 Google Maps - https://maps.app.goo.gl/Ymdgyh48LBDZYNVs5\n\nLink utili\nPagina del corso - \
https://linux.studenti.polito.it/wp/corso-gnu-linux-base-autunno-2022/\nRegistazioni delle lezioni (anno corrente e precedenti) - \
https://linux.studenti.polito.it/wp/video-corso-gnu-linux-base/\nCanale Telegram - https://t.me/corsolinuxpolito'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Wrapper functions
def send(update, message):
    chat_id = update.message.chat_id
    update.message.chat.bot.send_message(chat_id, message, parse_mode = 'HTML', disable_web_page_preview=True)
    logging.info('Sent:',message)

# Commands
def start(update, context):
    send(update, START)

def assistance(update, context):
    logging.info('Sending assistance info')
    send(update, ASSISTANCE)

def linuxbasic(update, context):
    logging.info('Sending basic course info')
    send(update, LINUX_BASIC)

def linuxadvanced(update, context):
    log('Sending advanced course info')
    send(update, LINUX_ADVANCED)


# Auxiliary
def extract(message, only_id=False):
    name = user = id = ''
    if not only_id:
        try:
            name += html.escape(message.from_user.first_name)
        except:
            name += ''
        try:
            name += ' ' + html.escape(message.from_user.last_name)
        except:
            name += ' '
        try:
            user = '@'+ html.escape(message.from_user.username)
        except:
            user = ''
    try:
        id = str(message.from_user.id)
    except:
        id = ''
    logging.info('Extracted:', id, user, name)
    return id, user, name

def main():
    # Updater
    logging.info('Setting up updater')
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Commands
    logging.info('Setting up commands')
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('sportello', assistance))
    dp.add_handler(CommandHandler('corsobase', linuxbasic))
    dp.add_handler(CommandHandler('corsoavanzato', linuxadvanced))

    # Set up the command list
    logging.info('Setting up command list')
    updater.bot.set_my_commands([ \
    ('sportello', 'Info sullo sportello di assistenza linux'), \
    ('corsobase', 'Info sul corso GNU/Linux base'), \
    ('corsoavanzato', 'Info sul corso GNU/Linux avanzato') \
    ])

    # Start bot
    logging.info('Starting bot')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

