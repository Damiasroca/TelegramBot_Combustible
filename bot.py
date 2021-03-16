import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext, PicklePersistence
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, Update
from mao import mao_2598, mao_2633, mao_2737, mao_13493, mao_13465, mao_13150, mao_2670
from ciuta import ciutadella_2667, ciutadella_2668, ciutadella_13088, ciutadella_13041, ciutadella_2569
from alaior import alaior_2590, alaior_2591, alaior_2669
from mercadal import mercadal_2666, mercadal_2645, mercadal_13267
from santlluis import santLluis_2580, santLluis_13028
from escastell import esCastell_13582
from ferreries import ferreries_2605




m_start = "Benvingut a *#MenorcaCombustibleBOT*.\nMés ⛽️ per menys 💶!\n"\
"Aquest bot notifica a demanda preus de combustible de totes ses estacions de servei de Menorca.\n"\
"Si m'envies es nom des municipi que vols consultar, et mostraré una llista de preus."

m_instruct = "Selecciona un municipi."

m_about = "*v0.2(beta)*\nEscrit per Damià Sintes Roca\nActualizat cada hora amb dades de\n_Ministerio de transición ecologica y reto demográfico_"

b1 = 'Maó'
b2 = 'Ciutadella'
b3 = 'Alaior'
b4 = 'Es Mercadal'
b5 = 'Sant Lluís'
b6 = 'Es Castell'
b7 = 'Ferreries'
b8 = 'Sobre...'
b9 = 'Municipis'



POBLES, TECLAT= range(2)

MAO, CIUTADELLA, ALAIOR, MERCADAL, ESCASTELL, SANTLLUIS, FERRERIES, AJUDA, MENU = range(9)


def start(update, context):

    update.message.reply_text(m_start, parse_mode=telegram.ParseMode.MARKDOWN)

    button1 = InlineKeyboardButton(
        b1, callback_data=str(MAO)
    )
    button2 = InlineKeyboardButton(
        b2, callback_data=str(CIUTADELLA)
    )
    button3 = InlineKeyboardButton(
        b3, callback_data=str(ALAIOR)
    )
    button4 = InlineKeyboardButton(
        b4, callback_data=str(MERCADAL)
    )
    button5 = InlineKeyboardButton(
        b5, callback_data=str(SANTLLUIS)
    )
    button6 = InlineKeyboardButton(
        b6, callback_data=str(ESCASTELL)
    )
    button7 = InlineKeyboardButton(
        b7, callback_data=str(FERRERIES)
    )
    button8 = InlineKeyboardButton(
        b8, callback_data=str(AJUDA)
    )

    update.message.reply_text(
            text = m_instruct, parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup = InlineKeyboardMarkup([
                [button1, button2, button3, button4],
                [button5, button6, button7, button8]
            ])
        )
    return POBLES

def start_over(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()

    button1 = InlineKeyboardButton(
        b1, callback_data=str(MAO)
    )
    button2 = InlineKeyboardButton(
        b2, callback_data=str(CIUTADELLA)
    )
    button3 = InlineKeyboardButton(
        b3, callback_data=str(ALAIOR)
    )
    button4 = InlineKeyboardButton(
        b4, callback_data=str(MERCADAL)
    )
    button5 = InlineKeyboardButton(
        b5, callback_data=str(SANTLLUIS)
    )
    button6 = InlineKeyboardButton(
        b6, callback_data=str(ESCASTELL)
    )
    button7 = InlineKeyboardButton(
        b7, callback_data=str(FERRERIES)
    )
    button8 = InlineKeyboardButton(
        b8, callback_data=str(AJUDA)
    )
    
    query.edit_message_text(
        text = m_instruct, parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup = InlineKeyboardMarkup([
            [button1, button2, button3, button4],
            [button5, button6, button7, button8]
        ])
    )
    return POBLES

def mao(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_mao_5 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                     "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((mao_2598['rotul']), (mao_2598['direccio']), (mao_2598['benzina']), (mao_2598['dieselA']), (mao_2598['dieselB']), (mao_2598['dieselPremium']), (mao_2598['GLP']), \
                                                                                                                         (mao_2737['rotul']), (mao_2737['direccio']), (mao_2737['benzina']), (mao_2737['dieselA']), (mao_2737['dieselB']), (mao_2737['dieselPremium']), (mao_2737['GLP']), \
                                                                                                                         (mao_2670['rotul']), (mao_2670['direccio']), (mao_2670['benzina']), (mao_2670['dieselA']), (mao_2670['dieselB']), (mao_2670['dieselPremium']), (mao_2670['GLP']), \
                                                                                                                         (mao_2633['rotul']), (mao_2633['direccio']), (mao_2633['benzina']), (mao_2633['dieselA']), (mao_2633['dieselB']), (mao_2633['dieselPremium']), (mao_2633['GLP']), \
                                                                                                                         (mao_13493['rotul']), (mao_13493['direccio']), (mao_13493['benzina']), (mao_13493['dieselA']), (mao_13493['dieselB']), (mao_13493['dieselPremium']), (mao_13493['GLP']), \
                                                                                                                         (mao_13465['rotul']), (mao_13465['direccio']), (mao_13465['benzina']), (mao_13465['dieselA']), (mao_13465['dieselB']), (mao_13465['dieselPremium']), (mao_13465['GLP']), \
                                                                                                                         (mao_13150['rotul']), (mao_13150['direccio']), (mao_13150['benzina']), (mao_13150['dieselA']), (mao_13150['dieselB']), (mao_13150['dieselPremium']), (mao_13150['GLP']))


    query.edit_message_text(
        text= missatge_mao_5, parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup = InlineKeyboardMarkup([
            [button9]
        ])
    )
    return TECLAT
    
def ciutadella(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_ciuta_5= "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                      "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                      "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                      "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                      "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((ciutadella_2569['rotul']), (ciutadella_2569['direccio']), (ciutadella_2569['benzina']), (ciutadella_2569['dieselA']), (ciutadella_2569['dieselB']), (ciutadella_2569['dieselPremium']),(ciutadella_2569['GLP']),\
                                                                                                                      (ciutadella_13041['rotul']), (ciutadella_13041['direccio']), (ciutadella_13041['benzina']), (ciutadella_13041['dieselA']), (ciutadella_13041['dieselB']), (ciutadella_13041['dieselPremium']), (ciutadella_13041['GLP']),\
                                                                                                                      (ciutadella_2668['rotul']), (ciutadella_2668['direccio']), (ciutadella_2668['benzina']), (ciutadella_2668['dieselA']), (ciutadella_2668['dieselB']), (ciutadella_2668['dieselPremium']), (ciutadella_2668['GLP']), \
                                                                                                                      (ciutadella_13088['rotul']), (ciutadella_13088['direccio']), (ciutadella_13088['benzina']), (ciutadella_13088['dieselA']), (ciutadella_13088['dieselB']), (ciutadella_13088['dieselPremium']), (ciutadella_13088['GLP']), \
                                                                                                                      (ciutadella_2667['rotul']), (ciutadella_2667['direccio']), (ciutadella_2667['benzina']), (ciutadella_2667['dieselA']), (ciutadella_2667['dieselB']), (ciutadella_2667['dieselPremium']), (ciutadella_2667['GLP']))

                        
                    
    query.edit_message_text(
                         text= missatge_ciuta_5, parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_markup = InlineKeyboardMarkup([
                             [button9]
                         ])
                     )
    return TECLAT

def sant(update, context= CallbackContext): 
    global poble_sant, betzina95_sant, dieselA_sant, rotul_sant, direccio_sant
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )

    missatge_santlluis1 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                         "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((santLluis_2580['rotul']), (santLluis_2580['direccio']), (santLluis_2580['benzina']), (santLluis_2580['dieselA']), (santLluis_2580['dieselB']), (santLluis_2580['dieselPremium']), (santLluis_2580['GLP']), \
                                                                                                        (santLluis_13028['rotul']), (santLluis_13028['direccio']), (santLluis_13028['benzina']), (santLluis_13028['dieselA']), (santLluis_13028['dieselB']), (santLluis_13028['dieselPremium']), (santLluis_13028['GLP']))
                    
                    
    query.edit_message_text(
                             text= missatge_santlluis1, parse_mode=telegram.ParseMode.MARKDOWN,
                             reply_markup = InlineKeyboardMarkup([
                                 [button9]

                                 ])
                         )
    return TECLAT
                
def escastell(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_escastell_1 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((esCastell_13582['rotul']), (esCastell_13582['direccio']), (esCastell_13582['benzina']), (esCastell_13582['dieselA']), (esCastell_13582['dieselB']), (esCastell_13582['dieselPremium']), (esCastell_13582['GLP']))

    query.edit_message_text(
                         text= missatge_escastell_1, parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_markup = InlineKeyboardMarkup([
                             [button9]
                         ])
                     )
    return TECLAT

def mercadal(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_mercadal_3 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                          "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                          "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((mercadal_2666['rotul']), (mercadal_2666['direccio']), (mercadal_2666['benzina']), (mercadal_2666['dieselA']), (mercadal_2666['dieselB']), (mercadal_2666['dieselPremium']), (mercadal_2666['GLP']),\
                                                                                                       (mercadal_2645['rotul']), (mercadal_2645['direccio']), (mercadal_2645['benzina']), (mercadal_2645['dieselA']), (mercadal_2645['dieselB']), (mercadal_2645['dieselPremium']), (mercadal_2645['GLP']), \
                                                                                                       (mercadal_13267['rotul']), (mercadal_13267['direccio']), (mercadal_13267['benzina']), (mercadal_13267['dieselA']), (mercadal_13267['dieselB']), (mercadal_13267['dieselPremium']), (mercadal_13267['GLP']))  

                    
    query.edit_message_text(
                         text= missatge_mercadal_3, parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_markup = InlineKeyboardMarkup([
                             [button9]
                         ])
                     )
    return TECLAT
                    
def alaior(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_alaior_3 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                        "🔹*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.\n\n"\
                        "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((alaior_2590['rotul']), (alaior_2590['direccio']), (alaior_2590['benzina']), (alaior_2590['dieselA']), (alaior_2590['dieselB']), (alaior_2590['dieselPremium']), (alaior_2590['GLP']),\
                                                                                                       (alaior_2591['rotul']), (alaior_2591['direccio']), (alaior_2591['benzina']), (alaior_2591['dieselA']), (alaior_2591['dieselB']), (alaior_2591['dieselPremium']), (alaior_2591['GLP']),\
                                                                                                       (alaior_2669['rotul']), (alaior_2669['direccio']), (alaior_2669['benzina']), (alaior_2669['dieselA']), (alaior_2669['dieselB']), (alaior_2669['dieselPremium']), (alaior_2669['GLP']))
                    

    query.edit_message_text(
                         text= missatge_alaior_3, parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_markup = InlineKeyboardMarkup([
                             [button9]
                         ])
                     )
    return TECLAT

def ferreries(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    
    missatge_ferreries_1 = "🔸*{}*\n_{}_\n\n- 95 Sense plom     = *{}* €\l  \n- Diesel A                 = *{}* €\l\n- Diesel B                 = *{}* €\l\n- Diesel Premium   = *{}* €\l\n- GLP                        = *{}* €\l.".format((ferreries_2605['rotul']), (ferreries_2605['direccio']), (ferreries_2605['benzina']), (ferreries_2605['dieselA']), (ferreries_2605['dieselB']), (ferreries_2605['dieselPremium']), (ferreries_2605['GLP']))
                    

    query.edit_message_text(
                         text= missatge_ferreries_1, parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_markup = InlineKeyboardMarkup([
                             [button9]
                         ])
                     )
    return TECLAT
                    
def sobre(update, context= CallbackContext):
    query = update.callback_query
    query.answer()
    button9 = InlineKeyboardButton(
        b9, callback_data=str(MENU)
    )
    query.edit_message_text(
        text= m_about, parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup = InlineKeyboardMarkup([
            [button9]
        ])
    )
    return TECLAT            

def main():

    persistence = PicklePersistence(filename='persistencia_bot')
    updater = Updater("TOKEN", persistence=persistence)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            POBLES:[
                CallbackQueryHandler(sant, pattern= str(SANTLLUIS)),
                CallbackQueryHandler(mao, pattern= str(MAO)),
                CallbackQueryHandler(ciutadella, pattern= str(CIUTADELLA)),
                CallbackQueryHandler(alaior, pattern= str(ALAIOR)),
                CallbackQueryHandler(mercadal, pattern= str(MERCADAL)),
                CallbackQueryHandler(escastell, pattern= str(ESCASTELL)),
                CallbackQueryHandler(ferreries, pattern= str(FERRERIES)),
                CallbackQueryHandler(sobre, pattern= str(AJUDA))
                ],
            TECLAT:[
                CallbackQueryHandler(start_over, pattern=str(MENU))
                ],
        },
        fallbacks=[CommandHandler('start_over', start_over)],
	    name="my_conversation",
        persistent=True,
    )
    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler('start', start))

    
    
 
  

    updater.start_polling()
    updater.idle()

main()
