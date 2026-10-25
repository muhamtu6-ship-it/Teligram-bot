import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Instagram sahifamga o'tish uchun quyidagi linkni bosing: https://www.instagram.com/muhammadazijj/")

if __name__ == '__main__':
    TOKEN = os.getenv('BOT_TOKEN')
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler(['start', 'salom'], start)
    application.add_handler(start_handler)
    
    application.run_polling()
