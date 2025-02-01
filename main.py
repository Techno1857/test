from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_API_TOKEN' with your actual bot token from BotFather
API_TOKEN = '7248397260:AAHIR9dQprGZhBdghyj8O1mLoxCrcvp-giU'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I\'m your test bot. Send /echo [message] and I\'ll repeat it.')

def echo(update: Update, context: CallbackContext) -> None:
    if context.args:
        text = ' '.join(context.args)
        update.message.reply_text(text)
    else:
        update.message.reply_text('Please provide a message to echo!')

def main():
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("echo", echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
