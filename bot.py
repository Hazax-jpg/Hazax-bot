lfrom telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot Hazax sudah aktif!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
