from telegram.ext import Updater

def main():
    mybot = Updater("7671951321:AAEed-2Y6wucqFDGfXFvVG4-YCZQygZOWoo", use_context=True)

    mybot.start_polling()
    mybot.idle()

main()