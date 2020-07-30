import telebot
from data import data
import config
from misc import class_search, class_search_markup

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    string, markup, images = data["На головну"]

    bot.send_message(
        message.chat.id,
        string,
        reply_markup=markup,
        parse_mode="HTML"
    )


@bot.message_handler(content_types=["text"])
def main(message):
    try:
        string, markup, images = data[message.text]
        bot.send_message(
            message.chat.id,
            string,
            reply_markup=markup,
            parse_mode="HTML"
        )
        if images:
            for image in images:
                with open(image, "rb") as im:
                    bot.send_photo(message.chat.id, im)
    except KeyError:
        if message.text[0] == "№":
            string = class_search(message.text)
            bot.send_message(
                message.chat.id,
                string,
                reply_markup=class_search_markup,
                parse_mode="HTML"
            )


bot.polling(none_stop=True)
