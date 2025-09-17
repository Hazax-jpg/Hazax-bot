from telegram.ext import Updater, CommandHandler

TOKEN = "8486763392:AAGpT0tanCSku1a1eDcWTnPEdue1RyJbF8c"

def start(update, context):
    update.message.reply_text("Hello Hazax 🚀! Bot awak dah aktif 24/7.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
