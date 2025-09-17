from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = "8486763392:AAGpT0tanCSku1a1eDcWTnPEdue1RyJbF8c"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Hazax 🚀! Bot awak dah aktif 24/7.")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Senarai command:\n/start - Mula bot\n/help - Bantuan")
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
