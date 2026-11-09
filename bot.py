import telebot
TOKEN = '9110296593:AAH2pg8K39sntWcxy1h9XjSoRFy4L-Xibog'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, 'اهلا بيك يا باشا 🕷️\nانا الباشا Spider، اكتب /ping وجربني')

@bot.message_handler(commands=['ping'])
def ping(m):
    bot.reply_to(m, 'pong! الباشا Spider شغال يا معلم')

bot.infinity_polling()
