import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configuration
API_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Set in Koyeb environment variables
PORT = int(os.getenv('PORT', 8000))      # Default port 8000 for local testing
PUBLIC_URL = os.getenv('PUBLIC_URL')     # Your Koyeb app URL (e.g., https://your-app.koyeb.app)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I\'m your deployed bot. Send /echo [message] and I\'ll repeat it.')

def echo(update: Update, context: CallbackContext) -> None:
    if context.args:
        text = ' '.join(context.args)
        update.message.reply_text(text)
    else:
        update.message.reply_text('Please provide a message to echo!')

def main():
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("echo", echo))

    # Webhook configuration for production
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=API_TOKEN,
        webhook_url=f"{PUBLIC_URL}/{API_TOKEN}"
    )
    updater.idle()

if __name__ == '__main__':
    main()
