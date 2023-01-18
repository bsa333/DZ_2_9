from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def del_abv(update, context):
    text = update.message.text.split()
    list1 =[]
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1))

def del_abvV2(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, "".join(list1[1:]))

hand_com = CommandHandler("filter", del_abvV2)
del_handler = MessageHandler(Filters.text, del_abv)


dispatcher.add_handler(del_handler)
dispatcher.add_handler(hand_com)

print("server start")

updater.start_polling()
updater.idle()
