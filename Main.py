TOKEN = "Your Telegram Bot token"
ch_id = "reciving channel id"
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import random, logging, json
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
#start updater and dispatcher
logging.basicConfig(filename='filename.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#start logging
from telegram import Update
ch_id= 0
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="welcome text")
#start updater and dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def send(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Next Submission will be sent")
    while True:
        context.bot.send_photo(chat_id=ch_id,photho=pht.jpg)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Submission Sent Successfully")
def file_handler (update, context):

    if update.message['photo'] == []:
        fileID = update.message['document']['file_id']
        fileName = update.message['document']['file_name']
        context.bot.sendDocument(chat_id = ch_id,
                                 caption = ' ',
                                 document = fileID)

    else:
        fileID = update.message['photo'][-1]['file_id']
        context.bot.sendPhoto(chat_id = ch_id,
                              caption = ' ',
                              photo = fileID)






start_handler = CommandHandler("send", send)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.document | Filters.photo, file_handler))

updater.start_polling()
